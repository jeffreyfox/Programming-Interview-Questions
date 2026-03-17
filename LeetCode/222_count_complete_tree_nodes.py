# TAGS: tree, binary tree

# Solution 1. Iterative approach
# Start with the maximum possible nodes of a perfect tree, then walk down and subtract the nodes that must be missing based on subtree heights.

# At each step, compare the right subtree height to determine whether the missing nodes lie on the right or left side.
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        height = left_height(root)
        total = (1 << height) - 1  # assume the tree is perfect: 2^h - 1 nodes

        # Walk down the tree and subtract missing nodes
        while root:
            height -= 1
            right_height = left_height(root.right)

            if right_height < height:
                # Right subtree is shorter than expected → nodes are missing there
                # Remove the missing portion from the perfect-tree count
                total -= (1 << right_height)
                root = root.left
            else:
                # Right subtree has full height → move to right subtree
                root = root.right

        return total

# Solution 2. Using recursion. Count by adding nodes up.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height(node) -> int:
            h = 0
            while node:
                node = node.left
                h += 1
            return h

        if root is None:
            return 0

        left_h = height(root.left)
        right_h = height(root.right)

        if left_h == right_h:
            # Left subtree is perfect
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # right subtree is perfect, but one level shorter
            return (1 << right_h) + self.countNodes(root.left)
