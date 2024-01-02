#!/usr/bin/python3
"""
0. UTF-8 Validation
"""


def validUTF8(data):
    """
    method that determines if given data set represents
    a valid utf-8 encoding
    """
    next_byte = 0
    for byte in data:
        if next_byte:
            if byte >> 6 != 0b10:
                return False
            next_byte -= 1
        else:
            if byte >> 7 == 0:
                next_byte = 0
            elif byte >> 5 == 0b110:
                next_byte = 1
            elif byte >> 4 == 0b1110:
                next_byte = 2
            elif byte >> 3 == 0b11110:
                next_byte = 3
            else:
                return False
    return next_byte == 0
