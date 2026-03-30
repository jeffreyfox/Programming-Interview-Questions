# TAGS: array,two pointer

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        # nums[0..j-1] != val
        # nums[j..i-1] == val
        # nums[i] TBD
        for i in range(len(nums)):
            if nums[i] != val:
                if i != j:
                    nums[j] = nums[i]
                j += 1
        return j