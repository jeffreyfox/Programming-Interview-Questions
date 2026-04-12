# TAGS: array

# Solution 1:
# Rotate the array to the right by k steps in-place.

# Idea:
# 1. Normalize k, because rotating by n steps is the same as no rotation.
# 2. Reverse the whole array.
# 3. Reverse the first k elements.
# 4. Reverse the remaining n-k elements.

# Example:
# nums = [1,2,3,4,5,6,7], k = 3
# -> reverse all      => [7,6,5,4,3,2,1]
# -> reverse first 3  => [5,6,7,4,3,2,1]
# -> reverse rest     => [5,6,7,1,2,3,4]
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        k = k % n

        def reverse(nums, lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

# Solution 2. Juggling method
# Treat rotation as moving each index to (i + k) % n.
# This creates gcd(n, k) independent cycles.
# For each cycle, carry values forward until we return to the start.
# Time: O(n), Space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        n = len(nums)
        k %= n
        if k == 0:
            return
        
        for i in range(math.gcd(n, k)):
            tmp = nums[i]
            j = i
            while True:
                j = (j + k) % n
                nums[j], tmp = tmp, nums[j]
                if j == i:
                    break