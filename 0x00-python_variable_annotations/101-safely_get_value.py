#!/usr/bin/env python3
"""module element length"""
from typing import Mapping, TypeVar, Any


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T = None):
    """safely get value"""
    if key in dct:
        return dct[key]
    else:
        return default
