# TAGS: DP

# Bottom-up DP solution
# Note that we loop over coins for better efficiency (not over all values from 1 to x)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[x] = minimum number of coins needed to make amount x
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], dp[x - c] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1