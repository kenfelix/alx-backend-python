#!/usr/bin/env python3
"""This module contains modules to return tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return  tuple"""
    return (k, pow(v, 2))
