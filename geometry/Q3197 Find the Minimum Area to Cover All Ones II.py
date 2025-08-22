# geometry - hard
from typing import List
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def findMinSquareArea(r1, c1, r2, c2, grid=grid):

            min_r, max_r = r2+1, r1-1
            min_c, max_c = c2+1, c1-1
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):

                    if grid[r][c] == 1:
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)

                        min_c = min(min_c, c)
                        max_c = max(max_c, c)

            return (max_r - min_r + 1) * (max_c - min_c + 1)

        ans = float('inf')

        # pure vertical
        for c1 in range(n-2):
            for c2 in range(c1+1, n-1):
                
                a1 = findMinSquareArea(0, 0, m-1, c1)
                a2 = findMinSquareArea(0, c1+1, m-1, c2)
                a3 = findMinSquareArea(0, c2+1, m-1, n-1)

                ans = min(ans, a1 + a2 + a3)

        # vertical first, then horizontal
        for c in range(n-1):
            for r in range(m-1):

                a1 = findMinSquareArea(0, 0, m-1, c)
                a2 = findMinSquareArea(0, c+1, r, n-1)
                a3 = findMinSquareArea(r+1, c+1, m-1, n-1)

                ans = min(ans, a1 + a2 + a3)

                a1 = findMinSquareArea(0, 0, r, c)
                a2 = findMinSquareArea(r+1, 0, m-1, c)
                a3 = findMinSquareArea(0, c+1, m-1, n-1)

                ans = min(ans, a1 + a2 + a3)

        # pure horizontal
        for r1 in range(m-2):
            for r2 in range(r1+1, m-1):

                a1 = findMinSquareArea(0, 0, r1, n-1)
                a2 = findMinSquareArea(r1+1, 0, r2, n-1)
                a3 = findMinSquareArea(r2+1, 0, m-1, n-1)

                ans = min(ans, a1 + a2 + a3)

        # horizontal first, then vertical
        for r in range(m-1):
            for c in range(n-1):

                a1 = findMinSquareArea(0, 0, r, n-1)
                a2 = findMinSquareArea(r+1, 0, m-1, c)
                a3 = findMinSquareArea(r+1, c+1, m-1, n-1)

                ans = min(ans, a1 + a2 + a3)

                a1 = findMinSquareArea(0, 0, r, c)
                a2 = findMinSquareArea(0, c+1, r, n-1)
                a3 = findMinSquareArea(r+1, 0, m-1, n-1)

                ans = min(ans, a1 + a2 + a3)

        return ans
    
grid = [[1,0,1],[1,1,1]]
grid = [[1,0,1,0],[0,1,0,1]]

Solution().minimumSum(grid)