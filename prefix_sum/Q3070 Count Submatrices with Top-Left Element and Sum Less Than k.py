# prefix sum - medium
from typing import List
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        # build a prefix sum of length n where pf_sum[i]
        # denotes the sum of grid[0...j][i] suppose we iterate up to j-th row
        pf_sum = [0] * n

        ans = 0
        for r in range(m):
            # for every row, track a running sum
            rSum = 0
            for c in range(n):
                pf_sum[c] += grid[r][c]
                rSum += pf_sum[c]

                if rSum <= k:
                    ans += 1

        return ans

grid, k = [[7,6,3],[6,6,1]], 18
grid, k = [[7,2,9],[1,5,0],[2,6,6]], 20

Solution().countSubmatrices(grid, k)