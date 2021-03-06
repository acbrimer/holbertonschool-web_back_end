#!/usr/bin/env python3
"""Module for testing util functions
"""

import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """TestGetJson class
    Tests utils.get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, uri, payload):
        """ Tests utils.get_json for expected value """
        with patch('requests.get') as r:
            r().json.return_value = payload
            self.assertEqual(get_json(uri), payload)


class TestMemoize(unittest.TestCase):
    """TestMemorize class
    Tests utils.memorize function
    """

    def test_memoize(self):
        """Tests memorize function """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_class = TestClass()
        test_class.a_method = MagicMock(return_value=42)
        self.assertEqual(test_class.a_property, 42)
        self.assertEqual(test_class.a_property, 42)
        test_class.a_method.assert_called_once()
