# prefix sum - medium
from typing import List
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) this question is a close duplicate of LC3070 
        # 2) build two prefix sums of X / Y frequencies for every col
        x_f, y_f = [0] * n, [0] * n

        ans = 0
        for r in range(m):

            x_total, y_total = 0, 0
            for c in range(n):

                if grid[r][c] == 'X':
                    x_f[c] += 1
                if grid[r][c] == 'Y':
                    y_f[c] += 1

                x_total += x_f[c]
                y_total += y_f[c]

                if x_total == y_total > 0:
                    ans += 1

        return ans
    
grid = [[".","."],[".","."]]
grid = [["X","X"],["X","Y"]]
grid = [["X","Y","."],["Y",".","."]]

Solution().numberOfSubmatrices(grid)