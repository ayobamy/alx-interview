#!/usr/bin/python3


def makeChange(coins, total):
    """
    return fewest number of `coins`
    needed to meet `total`
    """
    if (total == 0 or total < 0):
        return 0

    f_coins = []
    for i in range(total + 1):
        f_coins.append(float('inf'))
    f_coins[0] = 0

    # print(f_coins)

    for coin in coins:
        for i in range(coin, total + 1):
            f_coins[i] = min(f_coins[i], 1 + f_coins[i - coin])

    if f_coins[total] != float('inf'):
        return f_coins[total]
    else:
        return -1
