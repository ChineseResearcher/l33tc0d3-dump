# prefix sum - medium
from typing import List
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) compute row prefix sum
        # 2) iterate through all possible top-left coordinates
        # and use prefix sums to compute sum of an hourglass

        row_pf = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                row_pf[r][c] = (row_pf[r][c-1] if c > 0 else 0) + grid[r][c]

        ans = 0
        for r in range(m-2):
            for c in range(n-2):
                top_row = row_pf[r][c+2] - (row_pf[r][c-1] if c-1 >= 0 else 0)
                bot_row = row_pf[r+2][c+2] - (row_pf[r+2][c-1] if c-1 >= 0 else 0)
                ans = fmax(ans, top_row + bot_row + grid[r+1][c+1])

        return ans
    
grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]

Solution().maxSum(grid)