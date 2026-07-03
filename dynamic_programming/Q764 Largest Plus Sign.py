# dp - medium
from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:

        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) build prefix / suffix contiguous sum in all four directions
        # 2) update the cardinalMin[i][j] for all (i, j) as the largest
        # plus sign arm length
        mines = set(map(tuple, mines))
        cardinalMin = [ [float('inf')] * n for _ in range(n) ]

        # left-right
        def h_fill(start:int, end:int, step:int) -> None:
            for r in range(n):
                length = 0
                for c in range(start, end, step):
                    if not (0 <= c-step < n) or (r, c-step) in mines:
                        length = 0
                    else:
                        length += 1
                    cardinalMin[r][c] = fmin(cardinalMin[r][c], length)

        h_fill(0, n, 1)
        h_fill(n-1, -1, -1)

        # top-down
        def v_fill(start:int, end:int, step:int) -> None:
            for c in range(n):
                length = 0
                for r in range(start, end, step):
                    if not (0 <= r-step < n) or (r-step, c) in mines:
                        length = 0
                    else:
                        length += 1
                    cardinalMin[r][c] = fmin(cardinalMin[r][c], length)

        v_fill(0, n, 1)
        v_fill(n-1, -1, -1)

        ans = 0
        for r in range(n):
            for c in range(n):
                if (r, c) in mines:
                    continue
                ans = fmax(ans, 1 + cardinalMin[r][c])

        return ans
    
n, mines = 5, [[4,2]]
n, mines = 1, [[0,0]]
n, mines = 5, [[3,0],[3,3]]

Solution().orderOfLargestPlusSign(n, mines)