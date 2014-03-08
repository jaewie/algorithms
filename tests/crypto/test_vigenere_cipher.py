from crypto.vigenere_cipher import vigenere_cipher
import unittest

class TestVigenereCipher(unittest.TestCase):
    def test_empty(self):
      self.assertEquals('', vigenere_cipher('', ''))

    def test_vigenere(self):
      self.assertEquals('abc', vigenere_cipher('abc', 'aaa'))
      self.assertEquals('ace', vigenere_cipher('abc', 'abc'))
      self.assertEquals('bcd', vigenere_cipher('abc', 'bbb'))
      self.assertEquals('cde', vigenere_cipher('abc', 'ccc'))

    def test_longer_msg(self):
      self.assertEquals('cdefg', vigenere_cipher('abcde', 'c'))
