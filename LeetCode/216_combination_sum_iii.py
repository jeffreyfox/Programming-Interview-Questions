class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []

        beg = 1
        end = 9
        # pick kk numbers from from start to end to sum up to target
        def dfs(start, kk, target) -> None:
            if kk == 0:
                if target == 0:
                    result.append(path[:])
                return
            for i in range(start, end+1):
                if i > target:
                    break
                path.append(i)
                dfs(i+1, kk-1, target-i)
                path.pop()
            
        dfs(beg, k, n)
        return result
