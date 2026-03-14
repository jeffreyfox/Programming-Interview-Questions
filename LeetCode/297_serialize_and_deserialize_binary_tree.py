# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 2026.03.09. Solution 1.
# Use a nested inline dfs function in serialize and deserialize.
# In deserialize, use an iterator to iterate through the serialized string.

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "N"

        vals = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(","))

        def dfs() -> Optional[TreeNode]:
            val = next(vals)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# 2026.03.09. Solution 2. Use brackets to serialize and deserialize.
# The tree would look like: "(1(2()())(3(4()())(5()())))"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        parts = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                parts.append("()")
                return
            parts.append(f"({node.val})")
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return "".join(parts)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # returns new starting position
        def dfs(start: int) -> Tuple[Optional[TreeNode], int]:
            # Handles empty node
            if data[start:start+2] == "()":
                return None, start+2

            end = start
            # No need to find the matching closing bracket. Just needs to find the next ')'
            # because we are scanning the root now.
            while end < len(data) and data[end] != ')':
                end += 1

            node = TreeNode(int(data[start+1:end]))            
            node.left, next_start = dfs(end+1)
            node.right, next_start = dfs(next_start)
            return node, next_start

        root, _ = dfs(0)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))