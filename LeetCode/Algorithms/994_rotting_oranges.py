# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        (m, n) = len(grid), len(grid[0])
        num_fresh = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    num_fresh += 1
                elif v == 2:
                    q.append((i, j, 0))

        if num_fresh == 0:
            return 0

        level = 0
        while q:
            (i, j, level) = q.popleft()
            # Find four neighbors
            if self.check(i-1, j, m, n, level, grid, q):
                num_fresh -= 1
            if self.check(i, j-1, m, n, level, grid, q):
                num_fresh -= 1
            if self.check(i+1, j, m, n, level, grid, q):
                num_fresh -= 1
            if self.check(i, j+1, m, n, level, grid, q):
                num_fresh -= 1

        if num_fresh > 0:
            return -1
        return level

    # Returns whether a fresh orange is marked rotten
    def check(self, col, row, m, n, level, grid, q) -> bool:
        if col < 0 or col > m-1 or row < 0 or row > n-1:
            return False
        if grid[col][row] == 1:
            grid[col][row] = 2
            q.append((col, row, level+1))
            return True
        return False