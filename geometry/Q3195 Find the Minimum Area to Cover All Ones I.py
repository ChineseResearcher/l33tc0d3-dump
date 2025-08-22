# geometry - medium
from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        min_r, max_r = m, -1
        min_c, max_c = n, -1

        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1:
                    min_r = min(min_r, r)
                    max_r = max(max_r, r)

                    min_c = min(min_c, c)
                    max_c = max(max_c, c)

        return (max_r - min_r + 1) * (max_c - min_c + 1)
    
grid = [[0,1,0],[1,0,1]]
grid = [[1,0],[0,0]]

Solution().minimumArea(grid)