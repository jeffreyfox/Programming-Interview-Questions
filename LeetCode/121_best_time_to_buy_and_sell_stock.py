# TAGS: array,prefix sum,greedy
# Scan prices once
# Track the lowest price seen so far (best buy point)
# For each day, compute profit if selling today: price - lowest
# Update the maximum profit
# Return the best profit (or 0 if no profit possible)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return max_profit