#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened
    :param: boxes: list of boxes
        A key with the same number as a box opens that box
        You can assume all keys will be positive integers
        The first box boxes[0] is unlocked

    :return: True if all boxes can be opened, else return False
    """
    unlocked = [0]

    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
