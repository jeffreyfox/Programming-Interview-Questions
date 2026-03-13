# Iterative solution using unified method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        st.append((root, False))
        vals = []
        while st:
            node, visited = st.pop()
            if node is None:
                continue
            if not visited:
                st.append((node, True))
                st.append((node.right, False))
                st.append((node.left, False))
            else:
                vals.append(node.val)
        return vals