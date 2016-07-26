import unittest
from collection.bit_array import BitArray


class TestBitArray(unittest.TestCase):

    def setUp(self):
        self.array = BitArray()

    def test_get_on_empty_array(self):
        self.assertEquals(self.array.get(0), 0)

    def test_get_on_one_value_array(self):
        self.array.set(1)

        self.assertEquals(self.array.get(0), 0)
        self.assertEquals(self.array.get(1), 1)
        self.assertEquals(self.array.get(2), 0)

    def test_get_on_multi_value_array(self):
        self.array.set(3)
        self.array.set(5)
        self.array.set(5000)

        self.assertEquals(self.array.get(3), 1)
        self.assertEquals(self.array.get(4), 0)
        self.assertEquals(self.array.get(5), 1)
        self.assertEquals(self.array.get(6), 0)

        self.assertEquals(self.array.get(4999), 0)
        self.assertEquals(self.array.get(5000), 1)
        self.assertEquals(self.array.get(5001), 0)

    def test_set_on_empty_array(self):
        self.array.set(0)

        self.assertEquals(self.array.get(0), 1)


    def test_toggle_on_empty_array(self):
        self.array.toggle(0)

        self.assertEquals(self.array.get(0), 1)

    def test_clear_on_empty_array(self):
        self.array.clear(0)

        self.assertEquals(self.array.get(0), 0)

    def test_is_set_on_empty_array(self):
        self.assertFalse(self.array.is_set(0))
