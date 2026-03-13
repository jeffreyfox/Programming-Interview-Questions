# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        return vals


# Iterative solution. Push right child to stack first, then left child.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        st = []
        st.append(root)

        vals = []
        while st:
            node = st.pop()
            vals.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)

        return vals


# Iterative solution with unified method
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        st.append((root, False))
        vals = []
        while st:
            node, visited = st.pop()
            if node is None:
                continue
            if not visited:
                st.append((node.right, False))
                st.append((node.left, False))
                st.append((node, True))
            else:
                vals.append(node.val)
        return vals