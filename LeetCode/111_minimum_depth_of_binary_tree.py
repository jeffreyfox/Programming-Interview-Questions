# TAGS: tree,binary tree,recursion

# My solution (a bit verbose)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d_left = self.minDepth(root.left) if root.left else 0
        d_right = self.minDepth(root.right) if root.right else 0
        if d_left == 0 and d_right == 0:
            return 1
        if d_left > 0 and d_right > 0:
            return 1 + min(d_left, d_right)
        
        if d_left > 0:
            return 1 + d_left
        return 1 + d_right

# ChatGPT solution
# The main conceptual rule is simpler:
# if one child is missing, the minimum depth must come from the other child.
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

