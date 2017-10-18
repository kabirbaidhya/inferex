'''
Tests for our main inferex CLI module.
'''


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from inferex import __version__ as VERSION


class TestHelp(TestCase):

    def test_returns_usage_information(self):
        output = popen(['inferex', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['inferex', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):

    def test_returns_version_information(self):
        output = popen(['inferex', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
