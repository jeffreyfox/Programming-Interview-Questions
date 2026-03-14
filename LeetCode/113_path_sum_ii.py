# A cleaner solution:
# A cleaner pattern is:

# Always add node.val to path
# Always subtract from target
# Then check whether it's a valid leaf
# Backtrack once at the end

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        path = []
        result = []

        def dfs(node, target) -> None:
            if node is None:
                return

            path.append(node.val)
            target -= node.val
            if node.left is None and node.right is None:
                if target == 0:
                    result.append(path[:])
            else:
                dfs(node.left, target)
                dfs(node.right, target)
            # backtrack
            path.pop()
        
        dfs(root, targetSum)
        return result

# A less clean solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        path = []
        result = []

        def dfs(node, target) -> None:
            if node is None:
                return

            if node.left is None and node.right is None:
                if node.val == target:
                    path.append(node.val)
                    result.append(path[:])
                    path.pop()
                return
            
            target -= node.val
            path.append(node.val)
            dfs(node.left, target)
            dfs(node.right, target)
            path.pop()
        
        dfs(root, targetSum)
        return result