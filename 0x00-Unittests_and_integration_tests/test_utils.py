#!/usr/bin/env python3
"""Module for testing util functions
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    Class for testing nested map functions
    """
    @parameterized.expand([
        [{"a": 1}, ("a", ), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        [{}, ("a", ), 'a'],
        [{"a": 1}, ("a", "b"), 'b']
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """ Tests access_nested_map function raises correct execption """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual(str(err.exception),
                             "KeyError: '{}'".format(expected_key))
