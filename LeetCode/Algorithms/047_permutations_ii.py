# This solution uses backtracking to build permutations while tracking which elements are already used with a used array. At each step, it tries every unused number, adds it to the current path, recurses, and then backtracks.

# The key caveat is handling duplicates correctly. The array must be sorted first, and when encountering duplicate values, you should skip the current number only if the previous identical number has not been used in the current permutation (nums[idx] == nums[idx-1] and not used[idx-1]). This rule ensures duplicates are avoided while still allowing identical numbers to appear in different positions of valid permutations.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        used = [False] * n
        path = []
        result = []
        
        def dfs(k) -> None:
            if k == 0:
                result.append(path[:])
                return
            
            for idx in range(n):
                if used[idx]:
                    continue
                if idx > 0 and nums[idx] == nums[idx-1] and not used[idx-1]:
                    continue
                path.append(nums[idx])
                used[idx] = True
                dfs(k-1)
                path.pop()
                used[idx] = False
        
        dfs(n)
        return result