#!/usr/bin/env python3
"""
Module contains TestAccessNestedMap class.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """returns the expected output"""
        self.assertEqual(access_nested_map(map, path), expected_output)
        
    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """returns the expected output"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)

        self.assertEqual(str(e.exception)[1:-1], wrong_output)

