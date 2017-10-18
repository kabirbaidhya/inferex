from . import __version__
from .constants import NAME


def main():
    print('{} {}'.format(NAME, __version__))
