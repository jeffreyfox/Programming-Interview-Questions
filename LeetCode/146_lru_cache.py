# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
 

# Constraints:

# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.pos: dict[int, Node] = {}

    def insert_to_list(self, node: Node, prev: Node) -> None:
        next = prev.next
        prev.next = node
        node.next = next
        next.prev = node
        node.prev = prev

    def delete_from_list(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def get(self, key: int) -> int:
        # take the node out and put to the front (after dummy head)
        if key in self.pos:
            node = self.pos[key]
            self.delete_from_list(node)
            self.insert_to_list(node, self.head)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pos:
            node = self.pos[key]
            node.value = value # update value
            self.delete_from_list(node)
            self.insert_to_list(node, self.head)
        else:
            # new key
            node = Node(key, value)
            self.pos[key] = node
            self.insert_to_list(node, self.head)
        if len(self.pos) > self.capacity:
            # remove tail
            node_to_delete = self.tail.prev
            del self.pos[node_to_delete.key]
            self.delete_from_list(node_to_delete)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)