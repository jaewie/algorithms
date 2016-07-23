import unittest
from sequences.comparison_sorts import selection_sort


class TestComparisonSorts(unittest.TestCase):

    def test_select_sort_on_empty_list(self):
        self.assertEquals(selection_sort([]), [])


    def test_select_sort_on_one_element_list(self):
        self.assertEquals(selection_sort([1]), [1])


    def test_select_sort_on_multiple_element_list(self):
        lst = [1, 5, 3]
        self.assertEquals(selection_sort(lst), sorted(lst))


    def test_select_sort_on_sorted_list(self):
        lst = range(100)
        self.assertEquals(selection_sort(lst), range(100))

