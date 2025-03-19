# array - medium
class Solution:
    def isValidSudoku(self, board):
        def row_check(row):
    
            seen = set()
            for col in range(9):
                char = board[row][col]
                if char != '.':
                    if char in seen:
                        return False
                    seen.add(char)

            return True

        def col_check(col):

            seen = set()
            for row in range(9):
                char = board[row][col]
                if char != '.':
                    if char in seen:
                        return False
                    seen.add(char)

            return True

        def box_check(row, col):

            seen = set()
            for r in range(row, row+3):
                for c in range(col, col+3):
                    char = board[r][c]
                    if char != '.':
                        if char in seen:
                            return False
                        seen.add(char)

            return True

        # row checks
        for r in range(9):
            if not row_check(r):
                return False
            
        # # col checks
        for c in range(9):
            if not col_check(c):
                return False
            
        # box checks
        box_start = [[r,c] for r in range(0, 9, 3) for c in range(0, 9, 3)]
        for r, c in box_start:
            if not box_check(r,c):
                return False

        return True
    
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

Solution().isValidSudoku(board)