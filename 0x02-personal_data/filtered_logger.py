#!/usr/bin/env python3
""" Module for filter_datum """
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ filter_datum - was asked to use re and, technically, I did  """
    return "{};".format(separator.join(["{}={}".format(
        r[0],
        re.sub(r[1], redaction, r[1]) if r[0] in fields else r[1])
        for r in [s.split("=") for s in message.split(separator)][:-1]]))
