# TAGS: binary search tree,recursion,

# Solution 1: Track the min and max of subtrees iteratively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # also returns the min/max of the tree node values
        def is_valid(root: TreeNode) -> tuple[bool, int, int]:
            min_val = max_val = root.val
            if root.left:
                left_valid, left_min, left_max = is_valid(root.left)
                if not left_valid or left_max >= root.val:
                    return False, 0, 0
                min_val = left_min
            if root.right:
                right_valid, right_min, right_max = is_valid(root.right)
                if not right_valid or right_min <= root.val:
                    return False, -1, -1
                max_val = right_max
            return True, min_val, max_val

        valid, _, _ = is_valid(root)
        return valid

# Solution 2. A cleaner solution baces on low and high bounds:
# DFS with bounds:
# Each node must lie within a valid range (low, high).
# - For the left subtree, update upper bound to node.val
# - For the right subtree, update lower bound to node.val
#
# At each step, check:
#     low < node.val < high
#
# This enforces the BST property globally (not just parent-child).
#
# Time: O(n) — visit each node once
# Space: O(h) — recursion stack (h = tree height)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, lo, hi) -> bool:
            if not root:
                return True
            if not (lo < root.val < hi):
                return False
            
            return valid(root.left, lo, root.val) and valid(root.right, root.val, hi)
        
        return valid(root, float("-inf"), float("inf"))
