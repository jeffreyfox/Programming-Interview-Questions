# TAGS:two pointers,array,

# Use two pointers: j tracks the position to place the next non-zero.
# Iterate i through the array; when nums[i] != 0, swap it with nums[j].
# This keeps non-zero elements compacted at the front (stable order),
# and zeros naturally move to the end. When i == j, the swap is a no-op.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    # swap
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums

        