from setuptools import setup, find_packages

with open('README.rst') as fp:
    README = fp.read()

setup(
    name='tomato-libnotify',
    version='0.1',
    author='Sviatoslav Abakumov',
    author_email='dust.harvesting@gmail.com',
    description='The Pomodoro Technique® timer for Linux based on libnotify',
    long_description=README,
    url='https://github.com/Perlence/tomato-libnotify',
    download_url='https://github.com/Perlence/tomato-libnotify/archive/master.zip',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'tomato-libnotify = tomato_libnotify.tomato:main',
        ],
    },
    install_requires=[
        'attrs',
        'gbulb',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ]
)
