from setuptools import setup, find_packages

# with open('README.md') as fp:
#     README = fp.read()

setup(
    name='tomato-libnotify',
    version='0.1',
    author='Sviatoslav Abakumov',
    author_email='dust.harvesting@gmail.com',
    description='...',
    # long_description=README,
    url='https://github.com/Perlence/tomato-libnotify',
    download_url='https://github.com/Perlence/tomato-libnotify/archive/master.zip',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'tomato = tomato.tomato:main',
        ],
    },
    install_requires=[
        'attrs',
        'gbulb',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ]
)
