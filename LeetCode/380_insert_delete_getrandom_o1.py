# TAGS: design

# Use a dynamic array (self.data) + hashmap (val_to_idx) to support O(1) operations.
# - Insert: append to array and record index in hashmap.
# - Remove: swap target element with last element, update its index in hashmap,
#   then pop from array and delete from hashmap.
# - getRandom: return a random element from the array (uniform distribution).
#
# Invariant: for any value x, self.data[self.val_to_idx[x]] == x
# Time: O(1) average for all operations, Space: O(n)
class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        idx = self.val_to_idx.get(val)
        if idx is None:
            return False
        last_idx = len(self.data) - 1
        last_val = self.data[last_idx]
        if idx != last_idx:
            self.data[idx] = last_val
            self.val_to_idx[last_val] = idx
        self.data.pop()
        self.val_to_idx.pop(val, None)
        return True

    def getRandom(self) -> int:
        ridx = random.randrange(len(self.data))
        return self.data[ridx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()