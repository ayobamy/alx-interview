#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    determines if a given data set represents
    a valid UTF-8 encoding
    """
    iterator = 0

    for i in data:
        if iterator == 0:
            if i & 128 == 0:
                iterator = 0
            elif i & 224 == 192:
                iterator = 1
            elif i & 240 == 224:
                iterator = 2
            elif i & 248 == 240:
                iterator = 3
            else:
                return False
        else:
            if i & 192 != 128:
                return False
            iterator -= 1
    if iterator == 0:
        return True
    return False
