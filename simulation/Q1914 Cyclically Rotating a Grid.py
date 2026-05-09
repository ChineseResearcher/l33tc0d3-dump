# simulation - medium
from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        # our curr. first row and last row
        fr, lr = 0, m-1

        # our curr. first col and last col
        fc, lc = 0, n-1

        # helper to generate the perimeter indices
        def p_idx(fr: int, lr: int, fc: int, lc: int) -> List[int]:
            i = []
            for r in range(fr, lr+1):
                i.append((r,fc))
            for c in range(fc+1, lc+1):
                i.append((lr,c))
            for r in range(lr-1, fr-1, -1):
                i.append((r,lc))
            for c in range(lc-1, fc, -1):
                i.append((fr, c))
            return i

        # keep shrinking our perimeter bounds until it becomes invalid
        while lr > fr and lc > fc:

            # travel from top-left corner in anti-clockwise manner
            # and record all the values that are in this layer
            i = p_idx(fr, lr, fc, lc)

            val = [grid[r][c] for r, c in i]
            m = len(val)

            j = k % m
            # values after rotation
            rot_val = val[-j:] + val[:(m-j)]

            for j in range(m):
                r, c = i[j]
                grid[r][c] = rot_val[j]

            fr += 1
            lr -= 1

            fc += 1
            lc -= 1

        return grid

grid, k = [[40,10],[30,20]], 1
grid, k = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 4

Solution().rotateGrid(grid, k)