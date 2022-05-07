#!/usr/bin/env python3
"""
Module contains TestAccessNestedMap class.
"""
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": a}, ("a",), 3),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """returns the expected output"""
        self.assertEqual(access_nested_map(map, path), expected_output)

