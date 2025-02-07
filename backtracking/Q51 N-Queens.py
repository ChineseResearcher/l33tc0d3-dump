# backtracking - hard
class Solution:
    def backtrack(self, occupied, placed, rowStart):

        if len(placed) == self.n:
            template = ['.' * self.n for _ in range(self.n)]

            # iterate through all placed Q
            for r, c in placed:
                template[r] = template[r][:c] + 'Q' + template[r][c+1:]
            
            self.ans.append(template[:])
            return
        
        # for square-n board to have n queens placed
        # each row should have exactly one queen placed
        r = rowStart
        for c in range(self.n):
            # verify if the curr. pos is not under attack
            if r not in occupied['horizontal'] and c not in occupied['vertical'] \
            and (-r+c) not in occupied['left_diag'] and (r+c) not in occupied['right_diag']:
                
                # place the queen
                placed.append([r,c])
                occupied['horizontal'].add(r)
                occupied['vertical'].add(c)
                occupied['left_diag'].add(-r+c)
                occupied['right_diag'].add(r+c)
                
                self.backtrack(occupied, placed, rowStart+1)

                # backtracking
                placed.pop()
                occupied['horizontal'].discard(r)
                occupied['vertical'].discard(c)
                occupied['left_diag'].discard(-r+c)
                occupied['right_diag'].discard(r+c)

    def solveNQueens(self, n: int):
        self.n = n
        # board is a square one with side length n
        # and the game wants to place n queens on the board
        # s.t. amongst all the queens, they cannot attack one another
        # horizontally, vertically or diagonally

        # for (left) diagonal encoding, (-row + col) is the encoding formulation
        # e.g. row 0, col 0 corresponds to diagonal 0,
        # row 1, col 0 corresponds to diagonal -1
        # row 0, col 1 corresponds to diagonal 1
        # encoding ranges from (-n+1) to (n-1)

        # similarly, for right diagonal encoding using (row + col)
        # encoding ranges from 0 to (2n-2)

        occupied = {'vertical': set(), 'horizontal': set(), 'left_diag': set(), 'right_diag': set()}

        self.ans = []
        self.backtrack(occupied, [], 0)
        return self.ans
    
n = 1 # [['Q']]
n = 2 # no solution
n = 4

Solution().solveNQueens(n)