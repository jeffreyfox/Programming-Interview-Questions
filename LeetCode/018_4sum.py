# TAGS: array,two pointers,sorting

# Short summary of 4Sum solution:

# Sort the array, then fix two numbers (i, j)
# Use two pointers (k, l) to find the remaining two numbers
# Move pointers based on sum compared to target

# Dedup without a set:

# Skip duplicate values for i and j
# After finding a valid quadruplet, move both pointers and skip duplicates for k and l
# This avoids generating duplicates in the first place

# Pruning optimization:

# If the smallest possible sum is already > target → break early
# If the largest possible sum is still < target → skip

# 👉 Overall: sorting + two loops + two pointers + dedup + pruning = clean O(n^3) solution.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            # dedup for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # pruning for i
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue

            for j in range(i + 1, n - 2):
                # dedup for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # pruning for j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                k, l = j + 1, n - 1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]

                    if s == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        # dedup for k and l
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif s < target:
                        k += 1
                    else:
                        l -= 1

        return res