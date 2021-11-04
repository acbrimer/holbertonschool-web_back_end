#!/usr/bin/env python3
""" Module for 2-measure_runtime """
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime - calls async_comprehension x4, returns exec time """
    start: float = time()
    await asyncio.gather(
        *[async_comprehension() for i in range(4)])
    return (time() - start)
