from crypto.ciphers import caesar_cipher, one_time_pad, vigenere_cipher
import unittest


class TestCiphers(unittest.TestCase):

    def test_caesar_empty(self):
        self.assertEquals('', caesar_cipher('', 0))
        self.assertEquals('', caesar_cipher('', 5))
        self.assertEquals('', caesar_cipher('', -5))

    def test_caesar_shifting_right(self):
        self.assertEquals('bcd', caesar_cipher('abc', 1))
        self.assertEquals('cde', caesar_cipher('abc', 2))
        self.assertEquals('abc', caesar_cipher('abc', 26))

    def test_caesar_shifting_left(self):
        self.assertEquals('zab', caesar_cipher('abc', -1))
        self.assertEquals('yza', caesar_cipher('abc', -2))
        self.assertEquals('abc', caesar_cipher('abc', -26))

    def test_otp_empty(self):
        self.assertEquals('', one_time_pad(''))
        self.assertEquals('', one_time_pad('', []))
        self.assertEquals('', one_time_pad(''))

    def test_otp_shifts(self):
        self.assertEquals('abc', one_time_pad('abc', [0, 0, 0]))
        self.assertEquals('bcd', one_time_pad('abc', [1, 1, 1]))
        self.assertEquals('cde', one_time_pad('abc', [2, 2, 2]))

        self.assertEquals('zbc', one_time_pad('abc', [-1, 26, -26]))

    def test_vigenere_empty(self):
        self.assertEquals('', vigenere_cipher('', ''))

    def test_vigenere_same_str_sizes(self):
        self.assertEquals('abc', vigenere_cipher('abc', 'aaa'))
        self.assertEquals('ace', vigenere_cipher('abc', 'abc'))
        self.assertEquals('bcd', vigenere_cipher('abc', 'bbb'))
        self.assertEquals('cde', vigenere_cipher('abc', 'ccc'))

    def test_vigenere_longer_msg(self):
        self.assertEquals('cdefg', vigenere_cipher('abcde', 'c'))
