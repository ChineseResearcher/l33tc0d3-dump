# prefix sum - medium
from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        # build row / col prefix sums
        row_pf, col_pf = [0] * m, [0] * n

        TOTAL, pr, pc = 0, -1, -1
        for r in range(m):
            for c in range(n):
                TOTAL += grid[r][c]
                if c > pc:
                    row_pf[r] += grid[r][c]

                if r > pr:
                    col_pf[c] += grid[r][c]

                pc = c
                if c == n-1:
                    pr += 1
                    pc = -1

        rSum = 0
        for x in row_pf:
            rSum += x
            if rSum == TOTAL - rSum:
                return True
            
        rSum = 0
        for x in col_pf:
            rSum += x
            if rSum == TOTAL - rSum:
                return True
            
        return False
    
grid = [[1,4],[2,3]]
grid = [[1,3],[2,4]]

Solution().canPartitionGrid(grid)