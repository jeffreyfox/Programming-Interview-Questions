# TAGS: array,two pointers

# Solution 1. Adapted from 026
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        i = 0
        k = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            
            count = min(2, j-i)
            for _ in range(count):
                nums[k] = nums[i]
                k += 1
            i = j
        return k

# Simpler solution (adapted from LC26)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n <= 2:
            return n
        
        i = 1  # last valid index (we allow first two elements)

        for j in range(2, n):
            if nums[j] != nums[i - 1]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1