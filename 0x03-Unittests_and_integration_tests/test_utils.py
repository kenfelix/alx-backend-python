#!/usr/bin/env python3
"""
Module contains test modules for utils.py.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized

from utils import access_nested_map, get_json


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
        
        
class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """returns the expected outputfor get_json"""
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
