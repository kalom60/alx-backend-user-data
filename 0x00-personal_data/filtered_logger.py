#!/usr/bin/env python3
"""script that hide some parts of a string"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str):
    """return the a string with hiddening password and DOB"""
    for field in fields:
        pattern = re.search(field + "=(.*)" + separator, message).group(1)
        new_pattern = pattern.split(";")[0]
        message = re.sub(new_pattern, redaction, message)
    return message
