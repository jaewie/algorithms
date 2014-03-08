from crypto.one_time_pad import one_time_pad
import unittest

class TestOneTimePad(unittest.TestCase):
    def test_empty(self):
      self.assertEquals('', one_time_pad(''))
      self.assertEquals('', one_time_pad('', []))
      self.assertEquals('', one_time_pad(''))

    def test_shifts(self):
      self.assertEquals('abc', one_time_pad('abc', [0,0,0]))
      self.assertEquals('bcd', one_time_pad('abc', [1,1,1]))
      self.assertEquals('cde', one_time_pad('abc', [2,2,2]))

      self.assertEquals('zbc', one_time_pad('abc', [-1,26,-26]))

