# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

# The encoded string should be as compact as possible.

 

# Example 1:

# Input: root = [2,1,3]
# Output: [2,1,3]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The input tree is guaranteed to be a binary search tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The BST is serialized using preorder traversal (root → left → right), storing only node values
# separated by commas. Because the tree is a binary search tree, the structure can be uniquely
# reconstructed from preorder values without storing null markers.

# During deserialization, the values are read as a stream using an iterator. The tree is rebuilt
# recursively using BST value bounds: each node must fall within a (lower, upper) range determined
# by its ancestors. A one-element lookahead buffer holds the next value so the algorithm can check
# whether it belongs to the current subtree before consuming it.

# This approach reconstructs the tree in O(n) time, processes each value once, and avoids extra
# structures like null markers, index variables, or slicing.

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        vals = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        if not data:
            return None

        vals = iter(map(int, data.split(",")))
        lookahead = [next(vals, None)]

        def dfs(lower, upper) -> Optional[TreeNode]:
            val = lookahead[0]
            if val is None:
                return None
            if not (lower < val < upper):
                return None
            
            node = TreeNode(val)
            lookahead[0] = next(vals, None)
            node.left = dfs(lower, val)
            node.right = dfs(val, upper)
            return node
        
        return dfs(float("-inf"), float("inf"))


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans