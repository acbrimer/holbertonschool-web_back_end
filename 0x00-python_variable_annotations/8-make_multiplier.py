#!/usr/bin/env python3
""" Module for 8-make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function make_multiplier - returns a new func """
    return lambda n: n * multiplier
