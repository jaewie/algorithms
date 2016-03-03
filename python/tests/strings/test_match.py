import unittest
import random
from strings.match import match


class TestStringMatch(unittest.TestCase):

    def test_match_start(self):
        self.assertEquals(0, match('hello world', 'hello'))

    def test_match_end(self):
        self.assertEquals(6, match('hello world', 'world'))

    def test_match_none(self):
        self.assertEquals(-1, match('hello world', 'z'))

    def test_match_empty_target(self):
        self.assertEquals(-1, match('', 'z'))

    def test_match_empty_pattern(self):
        self.assertEquals(-1, match('hello world', 'z'))
