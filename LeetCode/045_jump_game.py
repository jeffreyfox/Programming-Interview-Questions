# TAGS: greedy,array,dynamic programming

# Greedy solution
# Greedy / BFS-level approach:
#
# We treat the array like levels in BFS, where each "jump" expands a range.
#
# Variables:
# - cur_end: the farthest index reachable with the current number of jumps
# - farthest: the farthest index reachable from all indices in the current range
#
# Algorithm:
# 1. Iterate through the array, updating `farthest = max(farthest, i + nums[i])`
# 2. When we reach the end of the current range (i == cur_end):
#    - we must make a jump
#    - increment jumps
#    - update cur_end = farthest (move to next range)
#
# Optimization:
# - If `farthest >= n - 1`, we can reach the end with one more jump → return early
#
# Intuition:
# - Each jump explores all reachable positions (like a BFS level)
# - We only "commit" to a jump when we finish exploring the current range
#
# Time: O(n)
# Space: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        farthest = 0
        cur_end = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            # optimization: early exit
            if farthest >= n - 1:
                return jumps + 1

            if i == cur_end:
                jumps += 1
                cur_end = farthest
    
        return jumps

# DP solution (will result in TLE)
# DP solution (bottom-up):
#
# Let dp[i] = minimum number of jumps needed to reach index i.
# Initialize dp[0] = 0 and all others = infinity.
#
# For each index i:
# - Try all jumps from i (i + 1 to i + nums[i])
# - Update dp[next] = min(dp[next], dp[i] + 1)
#
# This effectively relaxes all reachable positions from each index,
# similar to shortest path in an unweighted graph.
#
# Time: O(n^2) in worst case (each index may explore up to n neighbors)
# Space: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        
        return dp[-1]