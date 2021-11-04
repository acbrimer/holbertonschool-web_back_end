#!/usr/bin/env python3
""" Module for 1-concurrent_coroutines """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Function wait_n - calls wait_random n times """
    return await asyncio.gather(
        *[wait_random(i) for i in range(n)]
    )
