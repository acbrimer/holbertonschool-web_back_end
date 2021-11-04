#!/usr/bin/env python3
""" Module for 2-measure_runtime """
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime - calls async_comprehension x4, returns exec time """
    res = await asyncio.gather(
        *[async_comprehension() for i in range(2)]
    )
    return sum(sum(res, []))
