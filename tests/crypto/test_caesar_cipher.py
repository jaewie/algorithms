from crypto.caesar_cipher import caesar_cipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_empty(self):
      self.assertEquals('', caesar_cipher('', 0))
      self.assertEquals('', caesar_cipher('', 5))
      self.assertEquals('', caesar_cipher('', -5))

    def test_shifting_right(self):
      self.assertEquals('bcd', caesar_cipher('abc', 1))
      self.assertEquals('cde', caesar_cipher('abc', 2))
      self.assertEquals('abc', caesar_cipher('abc', 26))

    def test_shifting_left(self):
      self.assertEquals('zab', caesar_cipher('abc', -1))
      self.assertEquals('yza', caesar_cipher('abc', -2))
      self.assertEquals('abc', caesar_cipher('abc', -26))
