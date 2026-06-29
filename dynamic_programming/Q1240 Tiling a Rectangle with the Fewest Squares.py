# dp - hard
from typing import Tuple
from functools import cache
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:

        fmin = lambda a, b: a if a < b else b
        
        if n > m: n, m = m, n
        # key ideas:
        # 1) imagine we are playing the game of Tetris on a n x m board,
        # where n <= m, and that every falling block is strictly square
        # 2) we use a DP approach to this problem by memoizing the skyline
        # of our current board, which is a tuple of length m, with each
        # element going up to n
        # 3) we always place the next block at the lowest position of the
        # skyline, if there are multiple disjoint sections where the skyline
        # have minimum heights, we fill the leftmost one

        @cache
        def f(skyline: Tuple[int]) -> int:

            # convert to list to allow height modification
            skyline = list(skyline)
            minHeight = min(skyline)

            if minHeight == n: 
                return 0

            # leftmost lowest
            start = skyline.index(minHeight)

            res = float('inf')
            for end in range(start, m):
                
                # end of curr. contiguous block of minHeight
                if skyline[end] != minHeight:
                    break

                length = end - start + 1
                # violation of height bound
                if skyline[end] + length > n:
                    break
                
                newSkyline = skyline.copy()
                # update the skyline with the square block added
                for i in range(start, end+1):
                    newSkyline[i] += length
                # solve new subproblem
                res = fmin(res, 1 + f(tuple(newSkyline)))

            return res

        return f(tuple([0] * m))

n, m = 2, 3
n, m = 5, 8
n, m = 11, 13
n, m = 13, 13 # constraint

Solution().tilingRectangle(n, m)