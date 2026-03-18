# TAGS: tree,binary tree, recursion

# Solution without short circuiting
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # returns height and also whether it is balanced
        def dfs(node) -> tuple[int, bool]:
            if not node:
                return 0, True
            
            left_h, left_balanced = dfs(node.left)
            right_h, right_balanced = dfs(node.right)
            balanced = left_balanced and right_balanced and abs(right_h - left_h) <= 1
            h = 1 + max(left_h, right_h)
            return h, balanced
        
        _, balanced = dfs(root)
        return balanced

# Solution with short circuiting
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # returns height and also whether it is balanced
        def dfs(node) -> tuple[int, bool]:
            if not node:
                return 0, True
            
            left_h, left_balanced = dfs(node.left)
            if not left_balanced:
                return 0, False    # short-circuit
            right_h, right_balanced = dfs(node.right)
            if not right_balanced:
                return 0, False    # short-circuit
            balanced = abs(right_h - left_h) <= 1
            h = 1 + max(left_h, right_h)
            return h, balanced
        
        _, balanced = dfs(root)
        return balanced