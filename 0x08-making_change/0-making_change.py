#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    return fewest number of `coins`
    needed to meet `total`
    """
    if (total <= 0):
        return 0

    f_coins = [float('inf')] * (total + 1)
    f_coins[0] = 0
    # for i in range(total + 1):
    #     f_coins.append(float('inf'))
    # f_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            f_coins[i] = min(f_coins[i], 1 + f_coins[i - coin])

    if f_coins[total] != float('inf'):
        return f_coins[total]
    else:
        return -1
