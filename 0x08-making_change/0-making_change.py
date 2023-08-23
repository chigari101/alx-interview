#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins for each value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Loop through each value from 1 to the total
    for i in range(1, total + 1):
        # Calculate the minimum number of coins needed for the current value
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return the result for the total amount
    return min_coins[total] if min_coins[total] != float('inf') else -1
