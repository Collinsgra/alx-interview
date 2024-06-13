#!/usr/bin/python3
"""Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0"""


def minOperations(n):
    '''Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
    '''
    pasted_chars = 1
    clipboard = 0
    counter = 0

    while pasted_chars < n:
        if clipboard == 0:

            clipboard = pasted_chars
            counter += 1

        if pasted_chars == 1:
            # paste chars
            pasted_chars += clipboard
            counter += 1
            continue

        remaining = n - pasted_chars

        if remaining < clipboard:
            return 0

        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:

            clipboard = pasted_chars
            # paste chars
            pasted_chars += clipboard
            counter += 2
    if pasted_chars == n:
        return counter
    else:
        return 0
