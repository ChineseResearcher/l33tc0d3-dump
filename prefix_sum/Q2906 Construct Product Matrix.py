# prefix sum - medium
from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        MOD = 12345
        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) build 2-D prefix & suffix sum table by pre-processing the grid
        # 2) obtain the answer for (i, j) by referencing both prefix & suffix sum tables

        pfSum = [ [None] * n for _ in range(m) ]
        rSum = 1
        for r in range(m):
            for c in range(n):
                rSum *= grid[r][c]
                rSum %= MOD
                pfSum[r][c] = rSum

        sfSum = [ [None] * n for _ in range(m) ]
        rSum = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                rSum *= grid[r][c]
                rSum %= MOD
                sfSum[r][c] = rSum

        ans = [ [None] * n for _ in range(m) ]
        for r in range(m):
            for c in range(n):
                
                pf_prod = 1
                # determine the prefix cumulative product
                if c - 1 >= 0:
                    pfr, pfc = r, c-1
                else:
                    pfr, pfc = r-1, n-1

                if pfr >= 0:
                    pf_prod = pfSum[pfr][pfc]

                sf_prod = 1
                # determine the suffix cumulative product
                if c + 1 < n:
                    sfr, sfc = r, c+1
                else:
                    sfr, sfc = r+1, 0

                if sfr < m:
                    sf_prod = sfSum[sfr][sfc]

                ans[r][c] = (pf_prod * sf_prod) % MOD

        return ans 

grid = [[1,2],[3,4]]
grid = [[12345],[2],[1]]

Solution().constructProductMatrix(grid)