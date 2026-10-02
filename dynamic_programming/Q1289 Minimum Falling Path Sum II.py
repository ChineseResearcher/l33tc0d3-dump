# dp - hard
class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:

        n = len(grid)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) matrix DP with rolling copy, optimized w/ prefix & suffix min.

        dp = [grid[0][i] for i in range(n)]

        # helper to generate prefix & suffix min.
        def getMin(dp_arr: list[int]) -> tuple[list[int], list[int]]:
            pfMin, sfMin = [float('inf')] * n, [float('inf')] * n
            for i in range(1, n):
                pfMin[i] = fmin(pfMin[i - 1], dp_arr[i - 1])

            for i in range(n - 2, -1, -1):
                sfMin[i] = fmin(sfMin[i + 1], dp_arr[i + 1])

            return pfMin, sfMin

        for r in range(1, n):
            pfMin, sfMin = getMin(dp)

            new_dp = [float('inf')] * n
            for c in range(n):
                new_dp[c] = fmin(pfMin[c], sfMin[c]) + grid[r][c]
                
            dp = new_dp

        return min(dp)

grid = [[7]]
grid = [[1,2,3],[4,5,6],[7,8,9]]

Solution().minFallingPathSum(grid)