class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or \
                   board[i] - i == col - row or \
                   board[i] + i == col + row:
                    return False
            return True
        
        def solve(row, board):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    solve(row + 1, board)
                    board[row] = -1
        
        count = 0
        solve(0, [-1] * n)
        return count
