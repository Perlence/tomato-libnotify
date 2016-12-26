import argparse
import asyncio
from datetime import datetime
from pkg_resources import resource_filename

import attr
import gbulb
from gi.repository import Notify

DELAYS = {
    'work': 25 * 60,
    'break': 5 * 60,
    'long_break': 15 * 60,
    'snooze_break': 5 * 60,
    'snooze_work': 5 * 60,
}
ICON = resource_filename('tomato_libnotify', 'pomodoro.png')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--silent', action='store_true',
                        help="don't print time logs")
    args = parser.parse_args()

    Notify.init('Tomato')
    gbulb.install()
    loop = asyncio.get_event_loop()

    tomato = Tomato(silent=args.silent)
    try:
        loop.run_until_complete(tomato.run())
    except KeyboardInterrupt:
        pass
    finally:
        tomato.close()


@attr.s
class Tomato:
    notification = attr.ib(default=None)
    state = attr.ib(default='work')
    silent = attr.ib(default=False)

    @asyncio.coroutine
    def run(self):
        notifications = {
            'work': break_notification,
            'break': work_notification,
            'long_break': work_notification,
            'snooze_break': break_notification,
            'snooze_work': work_notification,
        }

        while True:
            if self.state == 'cancel':
                break

            action_future, cb = future_callback()
            self.notification = notifications[self.state](cb)
            self.notification.connect('closed', cb, self.notification.primary_action)

            delay = DELAYS[self.state]
            yield from asyncio.sleep(delay)

            self.notification.show()
            self.log()
            action = yield from action_future
            self.state = action.action_id

    def log(self):
        if self.silent:
            return
        print('{:%Y-%m-%d %H:%M:%S} - {}'
              .format(datetime.now(), self.notification.props.body))

    def close(self):
        if self.notification is not None:
            self.notification.close()


def break_notification(callback):
    notification = Notify.Notification.new('Tomato', "Work's done", ICON)
    notification.set_timeout(Notify.EXPIRES_NEVER)
    notification.primary_action = 'break'
    notification.add_action('break', 'Take a break', callback)
    notification.add_action('long_break', 'Take a long break', callback)
    notification.add_action('snooze_break', 'Work 5 more minutes', callback)
    return notification


def work_notification(callback):
    notification = Notify.Notification.new('Tomato', "Break's up", ICON)
    notification.set_timeout(Notify.EXPIRES_NEVER)
    notification.primary_action = 'work'
    notification.add_action('work', 'Back to work', callback)
    notification.add_action('snooze_work', 'Rest 5 more minutes', callback)
    return notification


def future_callback():
    future = asyncio.Future()

    def callback(notification, action_id, user_data=None):
        action = Action(notification, action_id, user_data)
        if not future.done():
            future.set_result(action)

    return future, callback


@attr.s
class Action:
    notification = attr.ib()
    action_id = attr.ib()
    user_data = attr.ib()


if __name__ == '__main__':
    main()
