# TAGS: DP,array

# Solution using DP.
# dp[i] = length of the longest increasing subsequence that ends at index i

# Transition:

# dp[i] = 1 + max(dp[j]) for all j < i and nums[j] < nums[i]

# If no such j exists, then dp[i] = 1.

# Time complexity: O(n2)
# Space complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] is the length of the longest subsequence that ends at nums[i]
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# O(nlgn) solution based on binary search
# Use patience sorting: maintain tails where tails[k] is the minimum ending value
# of any increasing subsequence of length k+1. Binary search ensures O(n log n).
# Don't fully understand this though.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for x in nums:
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        
        return len(tails)
