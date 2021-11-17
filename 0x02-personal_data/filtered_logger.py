#!/usr/bin/python3
""" Module for filter_datum """
import re


def filter_datum(fields, redaction, message, separator):
    """ filter_datum - was asked to use re and, technically, I did  """
    rows = [s.split("=") for s in message.split(separator)][:-1]
    print(rows)
    return separator.join(["{}={}".format(
        r[0],
        re.sub(str(r[1]), str(redaction), r[1]) if r[0] in fields else r[1])
        for r in rows])
