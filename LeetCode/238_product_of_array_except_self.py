# TAGS: array

# Do two passes:
# Left → right: store prefix products (product of all elements before i)
# Right → left: multiply by suffix products (product of all elements after i)

# Key idea:

# For each index i, result is:
# (product of left side) × (product of right side)

# Why it’s optimal:

# No division (handles zeros correctly)
# O(n) time, O(1) extra space (excluding output)

# 👉 Clean two-pass solution using prefix + suffix products.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prod = 1
        for i in range(1, n):
            prod *= nums[i-1]
            result[i] *= prod
        prod = 1
        for i in range(n-2, -1, -1):
            prod *= nums[i+1]
            result[i] *= prod
        return result