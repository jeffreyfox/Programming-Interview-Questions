# TAGS: Backtracking,DFS,Matrics

# Approach:
# - DFS + backtracking from each cell.
# - Match board[i][j] with word[k], mark visited in-place, explore 4 dirs, then restore.
#
# Complexity:
# - Time: O(m * n * 3^L)
# - Space: O(L) recursion depth
#
# Caveat (bug in original solution):
# - Base case `if k == len(word): return True` is incorrect.
# - It only succeeds after stepping past the last char, forcing an extra move.
# - Fails when the last char is matched at the current cell (e.g., [["A"]], "A").
#
# Fix:
# - After confirming match, return True if k == len(word) - 1.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = '.'

            for di, dj in offsets:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '.' and dfs(ni, nj, k + 1):
                    board[i][j] = tmp
                    return True

            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False