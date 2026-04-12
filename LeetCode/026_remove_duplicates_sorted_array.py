# TAGS: array,two pointers

# Solution using two pointers and a write pointer. Can be simplified (see next solution)
# Since the array is sorted, duplicates appear in consecutive blocks.
# Use two pointers:
# - i scans the array and identifies the start of each block
# - j advances to find the first different value (end of the block)
# Write one copy of each block to nums[k], then move to the next block.
# Time: O(n), Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        i, k = 0, 0
        while i < n:
            # j points to next index where value is not equal to nums[i]
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1
            nums[k] = nums[i]
            k += 1
            i = j
        return k
    
# Simpler solution using only two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        i = 0
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
