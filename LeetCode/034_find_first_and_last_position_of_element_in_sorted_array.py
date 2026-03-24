# TAGS: array,binary search

# Since the array is sorted, use binary search to find the target’s left and right boundaries.
# bisect_left finds the first occurrence position.
# bisect_right finds the index just after the last occurrence.
# If both indices are the same, the target does not exist.
# Otherwise the range is [left, right - 1].

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right-1]

# Custom implementation of bisect_left and bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search_left(nums, target):
            lo, hi = 0, len(nums)-1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo
        
        def binary_search_right(nums, target):
            lo, hi = 0, len(nums)-1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo
         
        left = binary_search_left(nums, target)
        right = binary_search_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right-1]

# ChatGPT solution which is slightly better
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1
        return [left, right]
