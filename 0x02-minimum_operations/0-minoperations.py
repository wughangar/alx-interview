#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
    """
    function that returns minimum operations of a function
    """
    if n < 2:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
