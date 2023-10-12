#!/usr/bin/python3
'''
The minimum operations coding challenge.
'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0

    # Initialize variables
    operations_count = 0
    clipboard = 0
    current_H_count = 1

    while current_H_count < n:
        if clipboard == 0:
            # Init (the first copy all and paste)
            clipboard = current_H_count
            current_H_count += clipboard
            operations_count += 2
        elif n - current_H_count > 0 and \
        (n - current_H_count) % current_H_count == 0:
            # Copy all and paste
            clipboard = current_H_count
            current_H_count += clipboard
            operations_count += 2
        elif clipboard > 0:
            # Paste
            current_H_count += clipboard
            operations_count += 1

    return operations_count
