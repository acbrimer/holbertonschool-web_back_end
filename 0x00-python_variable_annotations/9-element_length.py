#!/usr/bin/env python3
""" Module for 9-element_length """
from typing import List, Tuple


def element_length(lst: List[str]) -> Tuple[str, int]:
    return [(i, len(i)) for i in lst]
