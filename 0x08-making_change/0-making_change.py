#!/usr/bin/python3
"""Change making module."""

from typing import List


def makeChange(coins: List, total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.

    Retruns:
        total number of coins
    """
    if total <= 0:
        return 0
    totalRemainder = total
    numberOfCoinsUsed = 0
    coinIndex = 0
    sortedCoins = sorted(coins, reverse=True)  # Sort coins in descending order
    numberOfCoinsProvided = len(coins)

    while totalRemainder > 0:
        # if the total cannot be met by the coins provided
        if coinIndex >= numberOfCoinsProvided:
            return -1
        if totalRemainder - sortedCoins[coinIndex] >= 0:
            totalRemainder -= sortedCoins[coinIndex]
            numberOfCoinsUsed += 1
        else:
            coinIndex += 1
    return numberOfCoinsUsed
