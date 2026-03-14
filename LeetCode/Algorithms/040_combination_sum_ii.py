class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solution = []
        result = []

        n = len(candidates)
        # Pick from candidates's start idx to the end to form sum of target
        def dfs(start, target):
            if target == 0:
                result.append(solution[:])
                return
            
            # pick start
            for idx in range(start, n):
                # early stopping. With this, no need to check target < 0 earlier
                if candidates[idx] > target:
                    return
                # Need to skip duplicate numbers. Note the first condition (> start)
                if idx > start and candidates[idx] == candidates[idx-1]:
                    continue
                solution.append(candidates[idx])
                # now it's idx+1, different from idx in #39 combination sum
                dfs(idx+1, target-candidates[idx])
                solution.pop()
        
        dfs(0, target)
        return result