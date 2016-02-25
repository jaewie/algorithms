import unittest
from collection.dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    def setUp(self):
        self.arr = DynamicArray()

    def test_constructor(self):
        self.assertTrue(self.arr.is_empty())
        self.assertEquals(0, len(self.arr))

    def test_one_append(self):
        element = 1
        self.arr.append(element)

        self.assertFalse(self.arr.is_empty())
        self.assertEquals(1, len(self.arr))

    def test_multiple_appendes(self):
        elements = range(100)
        for element in elements:
            self.arr.append(element)

        self.assertFalse(self.arr.is_empty())
        self.assertEquals(len(elements), len(self.arr))

    def test_one_pop(self):
        element = 1
        self.arr.append(element)

        self.assertEquals(element, self.arr.pop())
        self.assertTrue(self.arr.is_empty())
        self.assertEquals(0, len(self.arr))

    def test_multiple_pops(self):
        elements = range(100)
        for element in elements:
            self.arr.append(element)

        for element in reversed(elements):
            self.assertEquals(element, self.arr.pop())
        self.assertTrue(self.arr.is_empty())
        self.assertEquals(0, len(self.arr))

    def test_pop_empty(self):
        self.assertRaises(IndexError, self.arr.pop)

    def test_pop_too_many(self):
        self.arr.append(1)
        self.arr.pop()

        self.assertRaises(IndexError, self.arr.pop)

    def test_find_empty(self):
        self.assertEquals(-1, self.arr.find(900))

    def test_get_empty(self):
        self.assertRaises(IndexError, self.arr.__getitem__, 30)

    def test_get_not_empty(self):
        element = 900
        self.arr.append(element)
        self.assertEquals(element, self.arr[0])

    def test_set_empty(self):
        self.assertRaises(IndexError, self.arr.__setitem__, 0, 30)

    def test_set_not_empty(self):
        self.arr.append(900)
        self.arr[0] = 0
        self.assertEquals(0, self.arr[0])

    def test_find_empty(self):
        lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        for e in lst:
            self.arr.append(e)

        for i, e in enumerate(lst):
            self.assertEquals(i, self.arr.find(e))
