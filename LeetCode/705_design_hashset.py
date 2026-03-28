# DESIGN: hash table,design

# Design:
# Use an array of buckets (separate chaining) to implement a hash set.
# - Hash function maps key → bucket index.
# - Each bucket stores keys that collide (list).
#
# Operations:
# - add: insert key if not already in bucket (O(k))
# - remove: scan bucket once and delete key (O(k))
# - contains: check if key exists in bucket (O(k))
#
# k = average bucket size (load factor n / m).
# Time: O(1) average with good hashing, O(n) worst case due to collisions.
# Space: O(n)
#
# Note: removal can be optimized to one pass; optionally swap-with-last to make deletion O(1).

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)        

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.buckets[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)