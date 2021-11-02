#!/usr/bin/env python3
""" Module for 7-to_kv """
from typing import Union, Tuple, cast


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function to_kv - returns tuple with k and v^2 """
    return (k, cast(v ^ 2, float))
