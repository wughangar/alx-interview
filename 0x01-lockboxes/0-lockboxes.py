#!/usr/bin/python3
"""
0. Lockboxes
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened

    args:
        boxes - list of lists
    """
    n = len(boxes)
    unlocked_boxes = [0]

    i = 0
    while i < len(unlocked_boxes):
        current_box = unlocked_boxes[i]
        for key in boxes[current_box]:
            if key < n and key not in unlocked_boxes:
                unlocked_boxes.append(key)
        i += 1
    return len(unlocked_boxes) == n
