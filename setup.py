"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from inferex import __version__


try:
    this_dir = abspath(dirname(__file__))
    with open(join(this_dir, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    # Handle file not found Exception.
    long_description = 'inferex - Yet another pythonic deployment tool built on top of fabric.'


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=inferex', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='inferex',
    version=__version__,
    description='InfereX - More information still yet to come.',
    long_description=long_description,
    url='https://github.com/kabirbaidhya/inferex',
    author='Kabir Baidhya',
    author_email='kabirbaidhya@gmail.com',
    license='MIT',
    keywords='inferex',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
    ],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'inferex=inferex.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
    include_package_data=True
)
