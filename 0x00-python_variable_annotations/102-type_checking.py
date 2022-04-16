#!/usr/bin/env python3
"""module element zoom array"""
from typing import Tuple, Union


def zoom_array(lst: Tuple, factor: Union[int, float] = 2) -> Tuple:
    """return"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
