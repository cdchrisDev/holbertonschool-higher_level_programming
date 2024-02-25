#!/usr/bin/python3
"""Unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Classes testing """

    def test_postive_list(self):
        """ Positive listing """
        self.assertEqual(max_integer([10, 5, 90, 45, 35]), 90)

    def test_negative_list(self):
        """ Negative listing """
        self.assertEqual(max_integer([-22, -17, -15, -13, -6]), -6)

    def test_error(self):
        """ Error testing """
        with self.assertRaises(TypeError):
            max_integer(['n', 8, 10])

    def test_none(self):
        """ None error testing """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        """ Empty list error """
        self.assertEqual(max_integer([]), None)

    def test_unique_int(self):
        """ Unique value test """
        self.assertEqual(max_integer([51]), 51)

    def test_ordered_list(self):
        """ Reversed func test """
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_reversed_list(self):
        """ order func test """
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_positive_and_negatives(self):
        """ positive and negative func test """
        self.assertEqual(max_integer([-3, 2, 5, -99]), 5)


if __name__ == "__main__":
    unittest.main()
