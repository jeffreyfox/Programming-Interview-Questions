# Early stopping at n-k+1.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination = []
        result = []

        def dfs(start, k) -> None:
            if k == 0:
                result.append(combination[:])
                return
            
            # Pick k numbers from start to n, can stop at n-k+1 inclusive
            for i in range(start, n-k+2):
                combination.append(i)
                dfs(i+1, k-1)
                combination.pop()

        dfs(1, k)
        return result