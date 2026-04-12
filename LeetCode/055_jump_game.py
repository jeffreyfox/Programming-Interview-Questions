# TAGS: DP,array

# Greedily track the farthest reachable index;
# if any index is unreachable, return false, otherwise check if we can reach the end.
# Think of it like expanding a reachable boundary:

# farthest = the rightmost position you can get to so far
# At each step:
# If you can reach i, you can extend reach to i + nums[i]
# If you cannot reach i, you're done (gap)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, nums[i] + i)
        return True

# DP solution (results in Time Limit Exceeded)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i] = True if we can reach index i
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[n-1]
        