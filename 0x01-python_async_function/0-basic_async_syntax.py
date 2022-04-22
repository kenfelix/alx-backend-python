#!/usr/bin/env python3
"""
Contains Awaitable asyc coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random number"""
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
