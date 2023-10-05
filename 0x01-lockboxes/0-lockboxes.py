#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened.
    '''
    unlocked_boxes = set()
    unlocked_boxes.add(0)

    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.extend(boxes[key])
    
    return len(unlocked_boxes) == len(boxes)
