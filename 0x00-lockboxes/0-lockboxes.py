#!/usr/bin/python3

"""
number of locked boxes

Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""
    new_list = [0]
    for key in new_list:
        for key_box in boxes[key]:
            if key_box not in new_list:
                if key_box < len(boxes):
                    new_list.append(key_box)

    if len(new_list) == len(boxes):
        return True
    return False
