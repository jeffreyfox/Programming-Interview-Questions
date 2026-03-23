# TAGS: array,two pointers,sorting,binary search

# Sort the array, fix one number i, and use two pointers (j, k) to scan the rest
# If the sum is too large → move k left
# If the sum is smaller than target → all pairs between j and k are valid, so add k - j to count and move j right

# Key insight:

# When nums[i] + nums[j] + nums[k] < target, sorted order guarantees every index between j+1 and k also works

# Pruning:

# If the smallest possible sum for current i is already ≥ target, we can stop early

# 👉 Overall: optimal O(n^2) solution using sorting + two pointers + counting trick.

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0

        count = 0
        for i in range(n-2):
            # pruning
            if nums[i] + nums[i+1] + nums[i+2] >= target:
                break
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s >= target:
                    k -= 1
                else:
                    count += (k-j)
                    j += 1
        return count


# n2lgn solution using binary search + pruning
# Note we provide the lo index in bisect_left instead of creating a new slice
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0

        count = 0
        for i in range(n-2):
            # pruning
            if nums[i] + nums[i+1] + nums[i+2] >= target:
               return count
            for j in range(i+1, n-1):
                # pruning
                if nums[i] + nums[j] + nums[j+1] >= target:
                   break
                v = target - (nums[i] + nums[j])
                idx = bisect.bisect_left(nums, v, j+1)
                count += (idx - (j+1))
                
        return count
