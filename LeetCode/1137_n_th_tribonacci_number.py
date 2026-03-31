# TAGS: DP

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0] * (n + 1)
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        prev_3 = 0
        prev_2 = prev_1 = 1
        result = 0
        for i in range(3, n+1):
            result = prev_3 + prev_2 + prev_1
            prev_3, prev_2, prev_1 = prev_2, prev_1, result
        return result
