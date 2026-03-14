# Iterative solution uwith backtracking
# Linear scans all previous queens when checking if a new position can place a queen.
class Solution:

    def generate_result(self, queens: List[int]) -> List[str]:
        result = []
        n = len(queens)
        for col in queens:
            s = ["."] * n
            s[col] = "Q"
            result.append("".join(s))
        return result

    # check if we can place queen at row i col j
    def can_place(self, queens, i, j) -> bool:
        # check if the previous queens can attack
        for ir in range(i):
            jc = queens[ir]
            if j == jc or abs(i - ir) == abs(j - jc):
                return False
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1] * n
        result = []

        # Place queens on row r
        def dfs(r: int) -> None:
            if r == n:
                result.append(self.generate_result(queens))
                return
            for c in range(n):
                if self.can_place(queens, r, c):
                    queens[r] = c
                    dfs(r+1)
                    queens[r] = -1

        dfs(0)
        return result

# Anothe solution that uses O(1) time to check can place (by using a set to track col,diagonal, and anti-diagonal)
# Three cases that can attack
# 1. same column
# 2. diagonal: c - r is the same, e.g. [1,2] and [2, 3]. They have the same difference of 1
# 3. anti-diagonal: c + r is the same, e.g. [1, 2] and [3, 0]. They have the same sum of 3.

class Solution:

    def generate_result(self, queens: List[int]) -> List[str]:
        result = []
        n = len(queens)
        for col in queens:
            s = ["."] * n
            s[col] = "Q"
            result.append("".join(s))
        return result

    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = [-1] * n
        result = []

        col_set = set()
        diag_set = set()
        anti_diag_set = set()

        # Place queens on row r
        def dfs(r: int) -> None:
            if r == n:
                result.append(self.generate_result(queens))
                return
            for c in range(n):
                if c in col_set or c - r in diag_set or r + c in anti_diag_set:
                    continue
                
                queens[r] = c
                col_set.add(c)
                diag_set.add(c - r)
                anti_diag_set.add(c + r)
                dfs(r+1)
                queens[r] = -1
                col_set.remove(c)
                diag_set.remove(c - r)
                anti_diag_set.remove(c + r)

        dfs(0)
        return result

