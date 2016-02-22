import unittest
import collection
from collection.deque import Deque


class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deque = Deque()

    def test_constructor(self):
        self.assertEqual(self.deque._head,  None)
        self.assertEqual(self.deque._tail,  None)
        self.assertEqual(self.deque._count, 0)

    def test_append(self):
        self.deque.append(0)

        self.assertEqual(self.deque._head.val, 0)
        self.assertEqual(self.deque._tail.val, 0)
        self.deque.append(1)
        self.assertEqual(self.deque._head.val, 0)
        self.assertEqual(self.deque._tail.val, 1)
        self.deque.append(2)
        self.assertEqual(self.deque._head.val, 0)
        self.assertEqual(self.deque._tail.val, 2)

    def test_appendleft(self):
        self.deque.appendleft(0)
        self.assertEqual(self.deque._head.val, 0)
        self.assertEqual(self.deque._tail.val, 0)
        self.deque.appendleft(1)
        self.assertEqual(self.deque._head.val, 1)
        self.assertEqual(self.deque._tail.val, 0)
        self.deque.appendleft(2)
        self.assertEqual(self.deque._head.val, 2)
        self.assertEqual(self.deque._tail.val, 0)

    def test_pop(self):
        self.assertRaises(IndexError, self.deque.pop)

        self.deque.append(0)
        self.assertEquals(0, self.deque.pop().val)

        self.deque.append(0)
        self.deque.append(1)
        self.deque.append(2)
        self.assertEquals(2, self.deque.pop().val)

    def test_popleft(self):
        self.assertRaises(IndexError, self.deque.popleft)
        self.deque.append(0)
        self.assertEquals(0, self.deque.popleft().val)
        self.deque.append(0)
        self.deque.append(1)
        self.deque.append(2)
        self.assertEquals(0, self.deque.popleft().val)
        self.assertEquals(1, self.deque.popleft().val)
        self.assertEquals(2, self.deque.popleft().val)
        self.assertRaises(IndexError, self.deque.popleft)

    def test_count(self):
        self.assertEquals(0, self.deque.count)
        self.deque.append(0)
        self.assertEquals(1, self.deque.count)
        self.deque.append(1)
        self.assertEquals(2, self.deque.count)
