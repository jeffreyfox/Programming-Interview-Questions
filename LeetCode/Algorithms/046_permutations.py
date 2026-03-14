# Solution using a used list to track items already used.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        used = [False] * n
        result = []

        # Pick k numbers 
        def dfs(k) -> None:
            if k == 0:
                result.append(path[:])  # copy
                return
            
            for idx in range(n):
                # pick nums[i] if not used
                if used[idx]:
                    continue
                path.append(nums[idx])
                used[idx] = True
                dfs(k-1)
                # backtrack
                path.pop()
                used[idx] = False
        
        dfs(n)
        return result
