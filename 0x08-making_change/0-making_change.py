#!/usr/bin/python3
""" making change using dynamic approach """

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large value (total + 1 is large enough)
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Update the dp array for each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still total + 1, it means it's not possible to make the total
    return dp[total] if dp[total] != total + 1 else -1
