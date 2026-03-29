# TAGS: DP,binary search tree

# Classic dynamic programming. 

# DP:
# dp[i] = number of unique BSTs that can be built with i nodes.
# For each possible root j in [1..i]:
# - left subtree has j-1 nodes
# - right subtree has i-j nodes
# So:
# dp[i] += dp[j-1] * dp[i-j]
#
# Time: O(n^2)
# Space: O(n)

class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] = number of unique BSTs that can be built with i nodes
        dp = [0] * (n + 1)
        dp[0] = 1
        if n >= 1:
            dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_size = root - 1
                right_size = nodes - root
                dp[nodes] += dp[left_size] * dp[right_size]

        return dp[n]