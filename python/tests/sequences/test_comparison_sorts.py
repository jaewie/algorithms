import unittest
from sequences.comparison_sorts import selection_sort


class TestComparisonSorts(unittest.TestCase):

    def test_select_sort_on_empty_list(self):
        self.assertEquals(selection_sort([]), [])

    def test_select_sort_on_one_element_list(self):
        self.assertEquals(selection_sort([1]), [1])

    def test_select_sort_on_multiple_element_list(self):
        self._test_sort(selection_sort, [1, 5, 3])

    def test_select_sort_on_sorted_list(self):
        self._test_sort(selection_sort, range(100))

    def test_select_sort_on_reverse_sorted_list(self):
        self._test_sort(selection_sort, list(reversed(range(100))))

    def _test_sort(self, sort_func, example_list):
        self.assertEquals(sort_func(example_list), sorted(example_list))

