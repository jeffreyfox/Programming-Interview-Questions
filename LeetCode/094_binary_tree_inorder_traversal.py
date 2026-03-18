# TAGS: tree,binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return vals

# Iterative solution.
# Unified solution that can be extended to preorder and postorder traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        st = []
        st.append((root, False))
        vals = []
        while st:
            node, visited = st.pop()
            if node is None:
                continue
            if not visited:
                st.append((node.right, False))
                st.append((node, True))
                st.append((node.left, False))
            else:
                vals.append(node.val)
        return vals
