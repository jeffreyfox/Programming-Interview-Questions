# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j) -> None:
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] != "1":
                return
            
            grid[i][j] = "v"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count

# Solution 2 using BFS.
# Notes that we need to mark the grid as visited at queue insertion time, not at pop time.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def bfs(i, j) -> None:
            q = deque()
            q.append((i, j))
            grid[i][j] = "v"

            while q:
                ir, jc = q.popleft()
                
                if ir > 0 and grid[ir-1][jc] == "1":
                    q.append((ir-1, jc))
                    grid[ir-1][jc] = "v"
                if jc > 0 and grid[ir][jc-1] == "1":
                    q.append((ir, jc-1))
                    grid[ir][jc-1] = "v"
                if ir < m-1 and grid[ir+1][jc] == "1":
                    q.append((ir+1, jc))
                    grid[ir+1][jc] = "v"
                if jc < n-1 and grid[ir][jc+1] == "1":
                    q.append((ir, jc+1))
                    grid[ir][jc+1] = "v"


            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        
        return count