# TAGS: array,sliding window

# Iterate on the right boundary to make it more readable

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += (nums[i] - nums[i-k])
            best_sum = max(best_sum, window_sum)
        return best_sum / k
        