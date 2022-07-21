#!/usr/bin/env python3
"""script that hide some parts of a string"""
import re
from typing import List
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """return the a string with hiddening password and DOB"""
    for field in fields:
        message = re.sub(
                field + "=.*?" + separator,
                field + "=" + redaction + separator,
                message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialize the class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method to format logRecord"""
        formatter = super(RedactingFormatter, self).format(record)
        message = filter_datum(
                self.fields,
                self.REDACTION,
                formatter, self.SEPARATOR)
        return message


def get_logger() -> logging.Logger:
    """function that creates logger for user data"""
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(stream_handler)
    log.propagate = False
    return logger
