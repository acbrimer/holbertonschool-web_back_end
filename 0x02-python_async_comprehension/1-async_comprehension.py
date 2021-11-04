#!/usr/bin/env python3
""" Module for 1-async_comprehension """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async_comprehension - calls & returns list from async_generator """
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    return result
