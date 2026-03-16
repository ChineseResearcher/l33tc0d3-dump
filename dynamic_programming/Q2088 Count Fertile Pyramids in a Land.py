# dp - hard
from typing import List
class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        fmin = lambda a, b: a if a < b else b
        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) solve for pyramid and inverse-pyramid separately

        # 2) when solving for pyramids, start scanning from the bottommost row
        # and denote dp[r][c] as the max. height of the pyramid if (r, c) is the apex

        # 3) solve for inverse-pyramid by inverting the grid upside down

        def solve(grid: List[List[int]]) -> int:

            # init. DP to be the same as grid
            dp = [grid[r][:] for r in range(m)] 

            ans = 0
            for r in range(m-2, -1, -1):
                for c in range(1, n-1):

                    skip = False
                    # check if we have the smallest height-2 pyramid first
                    for nr, nc in [(r,c), (r+1,c-1), (r+1,c), (r+1,c+1)]:
                        if grid[nr][nc] == 0:
                            skip = True
                            break

                    if skip: continue

                    dp[r][c] = fmin(dp[r+1][c-1], dp[r+1][c+1]) + 1
                    ans += dp[r][c] - 1

            return ans

        grid_inv = [grid[r][:] for r in range(m-1, -1, -1)]
        return solve(grid) + solve(grid_inv)

grid = [[1,1,1],[1,1,1]]
grid = [[0,1,1,0],[1,1,1,1]]
grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]

Solution().countPyramids(grid)