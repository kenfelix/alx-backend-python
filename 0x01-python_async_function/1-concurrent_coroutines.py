#!/usr/bin/env python3
"""
Contains Awaitable asyc coroutine
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def  wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    value = [wait_random(max_delay) for i in range(n)]
    value = asyncio.as_completed(value)
    value = [await i for i in value]
    return value
