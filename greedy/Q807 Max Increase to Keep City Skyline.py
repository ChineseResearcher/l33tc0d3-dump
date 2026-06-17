# greedy - medium
from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) process the grid once to find out max. height for each row / col
        # 2) greedily top-up height to each grid[r][c] when it is smaller than
        # both the rowMax and colMax for that (row, col)

        rMax = {i:0 for i in range(n)}
        cMax = {i:0 for i in range(n)}

        for r in range(n):
            for c in range(n):
                h = grid[r][c]
                rMax[r] = fmax(rMax[r], h)
                cMax[c] = fmax(cMax[c], h)

        ans = 0
        for r in range(n):
            for c in range(n):
                ans += fmax(fmin(rMax[r], cMax[c]) - grid[r][c], 0)

        return ans

grid = [[0,0,0],[0,0,0],[0,0,0]]
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

Solution().maxIncreaseKeepingSkyline(grid)