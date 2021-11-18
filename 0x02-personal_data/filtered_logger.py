#!/usr/bin/env python3
""" Module for filter_datum """
import re
from typing import List
import logging
import time


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ filter_datum - was asked to use re and, technically, I did  """
    return "{}{}".format(separator.join(["{}={}".format(
        r[0],
        re.sub(r[1], redaction, r[1]) if r[0] in fields else r[1])
        for r in [s.split("=") for s in message.split(separator)][:-1]]),
        separator)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.FLDS = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ format - formatter for logging """
        t = time.asctime(time.localtime())
        m = filter_datum(self.FLDS, self.REDACTION, record.msg, self.SEPARATOR)
        d = dict(zip(['name', 'levelname', 'asctime', 'message'],
                     [record.name, record.levelname, t, m]))
        record.msg = self.FORMAT % d
        return super(RedactingFormatter, self).format(record)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """ get_logger - returns a logger for user_data """
    out = logging.StreamHandler()
    out.setLevel(logging.INFO)
    out.propogate = False
    fmt = RedactingFormatter(
        fields=PII_FIELDS)
    out.setFormatter(fmt)
    user_logger = logging.getLogger('user_data')
    user_logger.addHandler(out)
    user_logger.propagate = False
    return user_logger
