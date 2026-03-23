# TAGS: array,divide and conquer,greedy

# Elegant O(n) solution:
# Scan the array and track the maximum subarray sum ending at each index.
# At each step, either extend the previous subarray if it helps,
# or start fresh at the current element if the previous sum is negative.
# Meanwhile, keep updating a global maximum over all positions.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_sum = max(max_sum, max_ending_here)
        return max_sum

# Divide and conquer approach: O(nlgn) complexity:
# A short summary:

# Recursively split the array into left and right halves
# The answer for a range is the max of:
# best subarray entirely in the left half
# best subarray entirely in the right half
# best subarray crossing the midpoint
# The crossing case is found by taking:
# the best suffix ending at mid
# plus the best prefix starting at mid + 1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def max_crossing_sum(lo, mid, hi) -> int:
            sum_left = 0
            max_sum_left = float("-inf")
            for i in range(mid, lo-1, -1):
                sum_left += nums[i]
                max_sum_left = max(max_sum_left, sum_left)
            sum_right = 0
            max_sum_right = float("-inf")
            for i in range(mid+1, hi+1):
                sum_right += nums[i]
                max_sum_right = max(max_sum_right, sum_right)
            return max_sum_left + max_sum_right

        # get sub arr for nums[lo, hi] inclusive
        def max_sum(lo, hi):
            if hi == lo:
                return nums[lo]
            
            mid = lo + (hi - lo) // 2
            max_left = max_sum(lo, mid)
            max_right = max_sum(mid+1, hi)
            max_crossing = max_crossing_sum(lo, mid, hi)
            return max(max_left, max_right, max_crossing)
        
        return max_sum(0, n-1)
