# TAGS: tree,binary tree

# Solution from ChatGPT that processes the tree level by level using BFS,
# avoiding the need to store (node, level) in the queue.
# For each level, it builds a temporary list of values, then conditionally reverses it
# based on a left_to_right flag that flips after every level. This keeps the traversal 
# logic clean and eliminates the need for a separate post-processing step, making the
# code more concise and idiomatic while maintaining O(n) time complexity.
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        q = deque([root])
        left_to_right = True

        while q:
            level_vals = []
            for _ in range(len(q)):
                node = q.popleft()
                level_vals.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if not left_to_right:
                level_vals.reverse()

            result.append(level_vals)
            left_to_right = not left_to_right

        return result

# My solution which has similar idea but less elegant
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        q = deque()
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if level == len(result):
                result.append([])
            result[-1].append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        
        # Now reverse order of odd layers
        for i, arr in enumerate(result):
            if i & 1:
                result[i].reverse()
        return result