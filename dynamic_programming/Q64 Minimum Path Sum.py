# dp - medium
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) bottom-up tabulation DP to transition from dp[r][c-1] and dp[r-1][c]
        # 2) track min. path sum from either option

        dp = [ [float('inf')] * n for _ in range(m) ]

        for r in range(m):
            for c in range(n):

                op1 = dp[r][c - 1] if c - 1 >= 0 else float('inf')
                op2 = dp[r - 1][c] if r - 1 >= 0 else float('inf')
                prev = fmin(op1, op2)

                dp[r][c] = grid[r][c] + (prev if prev < float('inf') else 0)

        return dp[-1][-1]

grid = [[1,2,3],[4,5,6]]
grid = [[1,3,1],[1,5,1],[4,2,1]]

Solution().minPathSum(grid)