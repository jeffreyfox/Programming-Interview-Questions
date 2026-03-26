# TAGS: DP

# Solution using the dp array
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = number of ways to reach step i
        dp = [0] * (n + 1)
        
        # base cases
        dp[0] = 1   # 1 way to stay at ground
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

# O(1) space solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a + b
        return b