#!/usr/bin/python3
""" 0. Change comes from within """


def makeChange(coins, total):
    """
    function that deterines the fewest number of coins
    needed to meet a given aount total
    args:
        coins: list of values of coins in possesion
        total: amount to be met
    returns:
        0 if total is 0
        number of coins used
    """
    if total <= 0:
        return 0

    store = [float('inf')] * (total + 1)
    store[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            store[i] = min(store[i], store[i - coin] + 1)

    return store[total] if store[total] != float('inf') else -1
