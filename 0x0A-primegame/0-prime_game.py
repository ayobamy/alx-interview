#!/usr/bin/python3
"""
Prime Game
"""


def primeNumbers(n):
    """
    Get all prime numbers within range
    """
    primeNos = []
    filterd = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filterd[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filterd[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
