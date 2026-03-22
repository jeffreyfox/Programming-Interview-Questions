# Time complexity is O(n^2) and space is O(1) aside from sorting.

# A short summary of the approach:

# Sort the array
# Fix one number at index i
# Use two pointers j and k to scan the remaining range
# Compute s = nums[i] + nums[j] + nums[k]
# Track the sum with the smallest absolute difference from target
# If s is too large, move k left; otherwise move j right
If s == target, return immediately since that is the best possible answer

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)

        min_diff = float("inf")
        ans = 0
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                diff = s - target
                if diff == 0:
                    return s
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    ans = s
                if diff > 0:
                    k -= 1
                else:
                    j += 1
        return ans