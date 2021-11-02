#!/usr/bin/env python3
""" Module for 9-element_length """


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function element_length - returns tuple array """
    return [(i, len(i)) for i in lst]
