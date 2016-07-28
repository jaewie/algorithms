import unittest
from data_mining.apriori import apriori


class TestApriori(unittest.TestCase):

    def test_happy_case(self):
        transactions = {100: {1, 3, 4},
                        200: {2, 3, 5},
                        300: {1, 2, 3, 5},
                        400: {2, 5},
                        500: {1, 3, 5}}
        min_support_count = 2
        expected = {(1, 3, 5): 2,
                    (2, 3, 5): 2}

        self.assertEquals(expected, apriori(transactions, min_support_count))
