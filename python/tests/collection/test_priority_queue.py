import unittest
import operator
import random
import string
from collection.priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue()

    def test_constructor(self):
        self.assertTrue(self.pq.is_empty())
        self.assertEquals(0, len(self.pq))

    def test_one_put(self):
        element = 'foo'
        priority = 350
        self.pq.put(element, priority)

        self.assertFalse(self.pq.is_empty())
        self.assertEquals(1, len(self.pq))

    def test_multiple_put(self):
        elements = range(100)
        priority = 350
        for element in elements:
            self.pq.put(element, priority)

        self.assertFalse(self.pq.is_empty())
        self.assertEquals(len(elements), len(self.pq))

    def test_one_get(self):
        element = 'foo'
        priority = 350
        self.pq.put(element, priority)

        self.assertEquals((element, priority), self.pq.get())
        self.assertTrue(self.pq.is_empty())
        self.assertEquals(0, len(self.pq))

    def test_multiple_gets_sorted(self):
        elements = string.lowercase
        priorities = range(len(elements))
        self._test_multiple_gets(elements, priorities)

    def test_multiple_gets_sorted_reversed(self):
        elements = string.lowercase
        priorities = range(len(elements))[::-1]
        self._test_multiple_gets(elements, priorities)

    def test_multiple_gets_random(self):
        trials = 10
        elements = string.lowercase
        priorities = range(len(elements))

        for _ in range(trials):
            random.shuffle(priorities)
            self._test_multiple_gets(elements, priorities)

    def test_get_empty(self):
        self.assertRaises(IndexError, self.pq.get)

    def test_get_too_many(self):
        self.pq.put('foo', 350)
        self.pq.get()

        self.assertRaises(IndexError, self.pq.get)

    def _test_multiple_gets(self, elements, priorities):
        expected_gets = sorted(zip(elements, priorities),
                               key=operator.itemgetter(1))

        for element, priority in zip(elements, priorities):
            self.pq.put(element, priority)

        for element, priority in expected_gets:
            self.assertEquals((element, priority), self.pq.get())
        self.assertTrue(self.pq.is_empty())
        self.assertEquals(0, len(self.pq))
