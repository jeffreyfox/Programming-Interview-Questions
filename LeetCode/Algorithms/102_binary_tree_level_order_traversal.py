# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = Deque()
        result = []
        q.append((root, 0))
        while q:
            node, lvl = q.popleft()
            if lvl == len(result):
                result.append([node.val])
            else:
                result[-1].append(node.val)
            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl+1))
        return result

