# Backtracking by row: Use DFS to place one queen per row. Try every column c in row r, recurse to the next row when the position is valid, and backtrack afterward.

# O(1) conflict checks with sets: Track used positions with three sets:

# col_set → occupied columns

# diag_set → main diagonals (c - r)

# anti_diag_set → anti-diagonals (r + c)
# This avoids scanning previous rows and makes validity checks O(1).

# No queens[] array needed: Since the problem only asks for the count, we don’t store board state or reconstruct solutions—just track constraints with sets.

# Use nonlocal count: Allows the DFS helper to increment the solution counter without returning values through recursion, keeping the code cleaner.

# Backtracking cleanup: After exploring a placement, remove the column and diagonal entries from the sets to restore the state before trying the next column.

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0

        col_set = set()
        diag_set = set()
        anti_diag_set = set()

        # Place queens on row r
        def dfs(r: int) -> None:
            nonlocal count
            if r == n:
                count += 1
                return
            for c in range(n):
                if c in col_set or c - r in diag_set or r + c in anti_diag_set:
                    continue
                
                col_set.add(c)
                diag_set.add(c - r)
                anti_diag_set.add(c + r)
                dfs(r+1)
                col_set.remove(c)
                diag_set.remove(c - r)
                anti_diag_set.remove(c + r)

        dfs(0)
        return count