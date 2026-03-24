# Since it allows infinite transactions, we simply add up all positive gains

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        max_profit = 0
        for i in range(n):
            if i > 0 and prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit