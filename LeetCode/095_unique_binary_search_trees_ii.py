# TAGS: binary search tree,DP

# Recursive + memoization:
# generate(lo, hi) returns all unique BSTs that can be built using values in [lo, hi].
# For each value as root, recursively generate all left subtrees from [lo, root-1]
# and all right subtrees from [root+1, hi], then combine every left/right pair.
#
# Base case:
# - empty range returns [None], so subtree combinations work naturally
#
# Memoization avoids recomputing the same interval multiple times.
#
# Time: proportional to the number of generated BSTs (Catalan-number output size)
# Space: memo + recursion stack + space for all generated trees

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        memo = {}

        def generate(lo: int, hi: int) -> List[Optional[TreeNode]]:
            if lo > hi:
                return [None]

            if (lo, hi) in memo:
                return memo[(lo, hi)]

            result = []
            for root_val in range(lo, hi + 1):
                left_trees = generate(lo, root_val - 1)
                right_trees = generate(root_val + 1, hi)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        result.append(root)

            memo[(lo, hi)] = result
            return result

        return generate(1, n)