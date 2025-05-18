# dp - hard
from functools import cache
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        @cache
        def recursive_paint(currCell, prevCol):

            # 1) currCell
            # represent the cells in col-wise direction, i.e. the cell in 
            # 2nd row of 2nc col is considered the 4-th cell (0-based indexing)

            # 2) prevCol
            # represent the colored status of prev. column using
            # 15 bits, e.g. 001_100_010_100_001
            # would mean that row1: B, row2: R, row3: G, row4: R, row5: B
            # printInBinary(prevCol)

            if currCell == cell_cnt:
                return 1
            
            # we need to access the relevant row's info
            r = currCell % m
            c = currCell // m

            # to paint a new cell, we have to avoid 
            # using the same color as the prev. col and prev. row
            prc, pcc = -1, -1

            # check prev. row color (if we are at row 1-4, not 0)
            if r > 0:

                for bit in range((r-1)*3, (r-1)*3 + 3):
                    if prevCol & (1 << bit) != 0:
                        # override prc if a colored prev. row is found
                        prc = bit % 3
                        break

            # check prev. col color (if we are at col 1 and further)
            if c > 0:

                for bit in range(r*3, r*3 + 3):
                    if prevCol & (1 << bit) != 0:
                        pcc = bit % 3
                        break

            # try all three colors, subject to the constraint that
            # it cannot be the same color as prc and pcc
            curr_ans = 0
            for next_color in [0,1,2]:
                if next_color != prc and next_color != pcc:
                    # we need to unset prev. column's color if it's colored
                    # prepare the "newCol" to be used in next recursion

                    newCol = prevCol
                    if pcc != -1:
                        newCol = prevCol & ~(1 << 3*r + pcc)
                    newCol |= (1 << 3*r + next_color)

                    curr_ans += recursive_paint(currCell+1, newCol)
                    curr_ans %= MOD

            return curr_ans

        cell_cnt = m * n
        MOD = int(1e9 + 7)

        return recursive_paint(0, 0)
    
m, n = 1, 1
m, n = 1, 2
m, n = 5, 5
# constraint, strangely it hits max. recursion depth here not in LC judge
# m, n = 5, 1000

Solution().colorTheGrid(m, n)