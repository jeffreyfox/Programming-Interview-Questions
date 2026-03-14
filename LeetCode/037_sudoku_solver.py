# Preload constraints from the initial board
# Before DFS begins, populate row_sets, col_sets, and box_sets with the digits already present so constraint checks are valid.

# Track empty cells upfront
# Build a list of (row, col) positions for "." cells and recurse using an index into this list to avoid rescanning the board each recursion.

# Use O(1) constraint checks
# Maintain row_sets, col_sets, and box_sets so candidate validity checks are constant time.

# Proper backtracking state management
# When placing a digit:

# write to the board

# add it to the three constraint sets
# When backtracking:

# reset the board cell

# remove the digit from all sets.

# Try all candidates before failing
# The DFS should only return False after trying all digits 1–9 for the current cell.

# Correct termination condition
# The puzzle is solved when the recursion index reaches len(empty).

# Modify the board in place
# The function should solve the board directly without needing to return it.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        empty = []
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                box = (r // 3) * 3 + (c // 3)
                s = board[r][c]
                if s == ".":
                    empty.append((r, c))
                else:
                    row_sets[r].add(s)
                    col_sets[c].add(s)
                    box_sets[box].add(s)

        def dfs(idx) -> bool:
            if idx == len(empty):
                return True
            r, c = empty[idx]
            box = (r // 3) * 3 + (c // 3)
            for val in "123456789":
                if val in row_sets[r] or val in col_sets[c] or val in box_sets[box]:
                    continue
                board[r][c] = val
                row_sets[r].add(val)
                col_sets[c].add(val)
                box_sets[box].add(val) 
                if dfs(idx+1):
                    return True
                board[r][c] = "."
                row_sets[r].remove(val)
                col_sets[c].remove(val)
                box_sets[box].remove(val)
            return False
    
        dfs(0)