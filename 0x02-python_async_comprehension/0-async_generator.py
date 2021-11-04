#!/usr/bin/env python3
""" Module for 0-async_generator """
import asyncio
from random import uniform
from typing import List


async def async_generator() -> List[float]:
    """ Function async_generator - generates a random list """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
