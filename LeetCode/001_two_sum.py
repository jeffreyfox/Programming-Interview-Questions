# TAGS: array,two pointers,sorting,hash table

# Method 1 using a hash table. O(n)
# We could also use two pointers by sorting the array first.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            res = target - val
            idx = d.get(res, -1)
            if idx >= 0:
                return [idx, i]
            d[val] = i
        return [-1, -1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index: Dict[int, int] = {}
        for i, value in enumerate(nums):
            idx = value_to_index.get(target-value, -1)
            if idx >= 0:
                return [idx, i]
            value_to_index[value] = i
        return [-1, -1]
