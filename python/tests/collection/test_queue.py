import unittest
from collection.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_constructor(self):
        self.assertTrue(self.q.is_empty())
        self.assertEquals(0, len(self.q))

    def test_one_enqueue(self):
        element = 'foo'
        self.q.enqueue(element)

        self.assertFalse(self.q.is_empty())
        self.assertEquals(1, len(self.q))

    def test_multiple_enqueue(self):
        elements = range(100)
        for element in elements:
            self.q.enqueue(element)

        self.assertFalse(self.q.is_empty())
        self.assertEquals(len(elements), len(self.q))

    def test_one_dequeue(self):
        element = 'foo'
        self.q.enqueue(element)

        self.assertEquals(element, self.q.dequeue())
        self.assertTrue(self.q.is_empty())
        self.assertEquals(0, len(self.q))

    def test_multiple_dequeues(self):
        elements = range(100)
        for element in elements:
            self.q.enqueue(element)

        for element in elements:
            self.assertEquals(element, self.q.dequeue())
        self.assertTrue(self.q.is_empty())
        self.assertEquals(0, len(self.q))

    def test_dequeue_empty(self):
        self.assertRaises(IndexError, self.q.dequeue)

    def test_dequeue_too_many(self):
        self.q.enqueue('foo')
        self.q.dequeue()

        self.assertRaises(IndexError, self.q.dequeue)
