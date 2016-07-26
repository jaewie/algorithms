import unittest
from graphs.trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_one_insert(self):
        self.trie.insert('hello')
        self.assertTrue(self.trie.exists('hello'))
        self.assertFalse(self.trie.exists('bye'))

    def test_multi_inserts(self):
        self.trie.insert('hello')
        self.trie.insert('hello world')

        self.assertTrue(self.trie.exists('hello'))
        self.assertTrue(self.trie.exists('hello world'))
        self.assertFalse(self.trie.exists('hello trie'))
        self.assertFalse(self.trie.exists('foo bar'))

    def test_elements(self):
        insert_strs = ['foo', 'foo bar', 'bar', 'abc']

        for s in insert_strs:
            self.trie.insert(s)
        self.assertEqual(sorted(insert_strs), sorted(self.trie.elements()))
