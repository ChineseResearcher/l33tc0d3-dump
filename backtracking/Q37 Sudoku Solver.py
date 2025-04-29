# backtracking - hard
from typing import List
class Solution:
    # helper to determine block
    def get_block(self, r, c):
        return r // 3 * 3 + c // 3 + 1

    def backtrack(self, idx, row_used, col_used, block_used):
    
        # guaranteed only one solution
        if idx == len(self.unfilled):
            # mark solved
            return True

        r, c = self.unfilled[idx]
        b = self.get_block(r, c)
        for digit in "123456789":
            
            if digit in row_used[r] or digit in col_used[c] or digit in block_used[b]:
                continue
                
            row_used[r].add(digit)
            col_used[c].add(digit)
            block_used[b].add(digit)
            # mark curr. decision
            self.board[r][c] = digit

            if self.backtrack(idx+1, row_used, col_used, block_used):
                return True

            # backtrack all states
            row_used[r].discard(digit)
            col_used[c].discard(digit)
            block_used[b].discard(digit)
            self.board[r][c] = "."

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # first list down all the unfilled positions on the board
        self.unfilled = []

        # maintain usage of numbers
        row_used = {r:set() for r in range(9)} 
        col_used = {c:set() for c in range(9)} 
        block_used = {b:set() for b in range(1, 10)}

        for r in range(9):
            for c in range(9):
                
                if board[r][c] == '.':
                    self.unfilled.append([r,c])
                else:
                    digit = board[r][c]
                    row_used[r].add(digit)
                    col_used[c].add(digit)
                    block_used[self.get_block(r,c)].add(digit)

        self.board = board
        self.backtrack(0, row_used, col_used, block_used) 
        # view modified board
        for r in self.board:
            print(r)

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

Solution().solveSudoku(board)