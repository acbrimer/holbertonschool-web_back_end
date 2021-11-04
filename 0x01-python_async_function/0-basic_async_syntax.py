#!/usr/bin/env python3
""" Module for 0-basic_async_syntax """
import asyncio
from typing import Union
from random import uniform



async def wait_random(max_delay: Union[int, None] = 10) -> float:
    """ Function wait_random - waits for random time """
    rand: float = uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand