#!/usr/bin/env python3
"""Using Regex to match data and obfusicate personal data"""


from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """A function that returns the log message obfuscated
    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character
        is separating all fields in the log line (message)
    """
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(pattern,
                  lambda match: match.group().split('=')[0] + '=' + redaction,
                  message)
