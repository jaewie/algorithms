import unittest
import random
from collection.set import Set


class TestSet(unittest.TestCase):

    def setUp(self):
        self.set = Set()

    def test_constructor(self):
        self.assertTrue(self.set.is_empty())
        self.assertEquals(0, len(self.set))

    def test_one_add(self):
        element = 'foo'
        self.set.add(element)

        self.assertFalse(self.set.is_empty())
        self.assertEquals(1, len(self.set))
        self.assertTrue(self.set.exists(element))

    def test_multiple_adds(self):
        elements = range(100)
        for element in elements:
            self.set.add(element)

        for element in elements:
            self.assertTrue(self.set.exists(element))
        self.assertFalse(self.set.is_empty())
        self.assertEquals(len(elements), len(self.set))

    def test_clear(self):
        elements = range(100)
        for element in elements:
            self.set.add(element)
        self.set.clear()
        self.test_constructor()

    def test_one_remove(self):
        element = 'foo'
        self.set.add(element)
        self.set.remove(element)

        self.assertTrue(self.set.is_empty())
        self.assertEquals(0, len(self.set))
        self.assertFalse(self.set.exists(element))

    def test_multiple_removes(self):
        elements = range(100)
        for element in elements:
            self.set.add(element)

        for element in elements:
            self.set.remove(element)

        for element in elements:
            self.assertFalse(self.set.exists(element))

        self.assertTrue(self.set.is_empty())
        self.assertEquals(0, len(self.set))

    def test_remove_empty(self):
        self.assertRaises(KeyError, self.set.remove, 'foo')

    def test_remove_too_many(self):
        element = 'foo'
        self.set.add(element)
        self.set.remove(element)

        self.assertRaises(KeyError, self.set.remove, element)

    def test_remove_empty(self):
        self.assertRaises(KeyError, self.set.remove, 'foo')

    def test_merge_empty_sets(self):
        self.assertEquals(Set().merge(Set()), Set())

    def test_merge_multiple_elements(self):
        lst0 = [1, 2, 3]
        lst1 = [11, 12, 13]
        lst2 = [13]

        set0 = Set(lst0)
        set1 = Set(lst1)
        set2 = Set(lst2)

        self.assertEquals(set0.merge(set1), Set(lst0 + lst1))
        self.assertEquals(set1.merge(set2), set1)

    def test_diff_empty_sets(self):
        self.assertEquals(Set().diff(Set()), Set())

    def test_diff_multiple_elements(self):
        lst0 = [1, 2, 3]
        lst1 = [11, 12, 13]
        lst2 = [13]
        lst3 = [11, 12]

        set0 = Set(lst0)
        set1 = Set(lst1)
        set2 = Set(lst2)
        set3 = Set(lst3)

        self.assertEquals(set0.diff(set1), set0)
        self.assertEquals(set1.diff(set0), set1)
        self.assertEquals(set1.diff(set2), set3)
        self.assertEquals(set2.diff(set1), Set())

    def test_eq_empty(self):
        self.assertTrue(Set() == Set())

    def test_eq_not_empty(self):
        set0 = Set([1, 2, 3])
        set1 = Set([1, 2, 3])
        set2 = Set([4, 5, 6])

        self.assertTrue(set0 == set0)
        self.assertTrue(set1 == set1)
        self.assertTrue(set2 == set2)

        self.assertFalse(set0 == Set())
        self.assertFalse(Set() == set0)

        self.assertTrue(set0 == set1)
        self.assertTrue(set1 == set0)

        self.assertFalse(set0 == set2)
        self.assertFalse(set2 == set0)

        self.assertFalse(set1 == set2)
        self.assertFalse(set2 == set1)
