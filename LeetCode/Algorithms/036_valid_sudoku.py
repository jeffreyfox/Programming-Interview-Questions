# 1 pass solution using a single set but different row/col/box key prefixes
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue
                
                row_key = f"r{i}{c}"
                col_key = f"c{j}{c}"
                box = (i // 3) * 3 + (j // 3)
                box_key = f"b{box}{c}"
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True

# 1 pass solution using 9*3 = 27 sets
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue
                box = (i // 3) * 3 + (j // 3)
                if c in row_sets[i] or c in col_sets[j] or c in box_sets[box]:
                    return False
                row_sets[i].add(c)
                col_sets[j].add(c)
                box_sets[box].add(c)
        return True

# 3 pass solution using a set:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_row(row: int) -> bool:
            seen = set()
            for col in range(0, 9):
                c = board[row][col]
                if c == ".":
                    continue
                if c in seen:
                    return False
                seen.add(c)
            return True
        
        def check_col(col: int) -> bool:
            seen = set()
            for row in range(0, 9):
                c = board[row][col]
                if c == ".":
                    continue
                if c in seen:
                    return False
                seen.add(c)
            return True

        def check_block(self, block: int) -> bool:
            seen = set()
            start_row = (block // 3) * 3
            start_col = (block % 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    c = board[i][j]
                    if c == ".":
                        continue
                    if c in seen:
                        return False
                    seen.add(c)
            return True
   
        for i in range(0, 9):
            if not check_row(i):
                return False
            if not check_col(i):
                return False
            if not check_block(i):
                return False
        return True
