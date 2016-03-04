import unittest
from strings.match import match


class TestStringMatch(unittest.TestCase):

    def test_match_start(self):
        self._test_example('hello world', 'hello')

    def test_match_end(self):
        self._test_example('hello world', 'world')

    def test_match_none(self):
        self._test_example('hello world', 'z')

    def test_match_empty_target(self):
        self._test_example('', 'z')

    def _test_example(self, target, pattern):
        self.assertEquals(target.find(pattern), match(target, pattern))
