# TAGS: design

# Design:
# Track row sums, column sums, and two diagonals instead of storing the board.
# Use +1 for player 1 and -1 for player 2.
#
# On each move:
# - Add val to corresponding row, column, and (if applicable) diagonal(s).
# - If any absolute sum reaches n, that player wins.
#
# This works because a full line by one player results in sum = ±n.
#
# Time: O(1) per move
# Space: O(n)

class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = [0] * 2

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1
        self.rows[row] += val
        if abs(self.rows[row]) == self.n:
            return player
        self.cols[col] += val
        if abs(self.cols[col]) == self.n:
            return player
        if row == col:
            self.diagonal[0] += val
            if abs(self.diagonal[0]) == self.n:
                return player
        if row + col == self.n - 1:
            self.diagonal[1] += val
            if abs(self.diagonal[1]) == self.n:
                return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)