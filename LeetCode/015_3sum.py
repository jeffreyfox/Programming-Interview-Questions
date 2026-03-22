# TAGS: array,two pointers,sorting

# Short summary of optimal 3Sum solution:

# Sort the array, then fix one number nums[i] and use two pointers (j, k) to find pairs that sum to -nums[i].
# Move pointers based on the sum:
# If too small → move j right
# If too large → move k left
# If equal → record the triplet, then move both pointers

# Dedup without a set:

# Skip duplicate i values (if nums[i] == nums[i-1]: continue)
# After finding a valid triplet, skip duplicate values for j and k using while loops
# This ensures we never generate duplicate triplets in the first place

# Important detail:

# We cannot stop after finding one match for a given i
# There may be multiple valid pairs, so we must continue moving both pointers and keep searching within the same loop

# 👉 Overall: sorting + two pointers + careful duplicate skipping = O(n²) solution without extra space.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(0, n-2):
            # dedup
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, n-1
            target = -nums[i]
            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # dedup
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif s > target:
                    k -= 1
                else:
                    j += 1
        
        return result