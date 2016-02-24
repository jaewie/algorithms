import unittest
from collection.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_constructor(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEquals(0, len(self.stack))

    def test_one_push(self):
        element = 'foo'
        self.stack.push(element)

        self.assertFalse(self.stack.is_empty())
        self.assertEquals(1, len(self.stack))

    def test_multiple_pushes(self):
        elements = range(100)
        for element in elements:
            self.stack.push(element)

        self.assertFalse(self.stack.is_empty())
        self.assertEquals(len(elements), len(self.stack))

    def test_one_pop(self):
        element = 'foo'
        self.stack.push(element)

        self.assertEquals(element, self.stack.pop())
        self.assertTrue(self.stack.is_empty())
        self.assertEquals(0, len(self.stack))

    def test_multiple_pops(self):
        elements = range(100)
        for element in elements:
            self.stack.push(element)

        for element in reversed(elements):
            self.assertEquals(element, self.stack.pop())
        self.assertTrue(self.stack.is_empty())
        self.assertEquals(0, len(self.stack))

    def test_pop_empty(self):
        self.assertRaises(IndexError, self.stack.pop)

    def test_pop_too_many(self):
        self.stack.push('foo')
        self.stack.pop()

        self.assertRaises(IndexError, self.stack.pop)

    def test_peek_empty(self):
        self.assertRaises(IndexError, self.stack.peek)
