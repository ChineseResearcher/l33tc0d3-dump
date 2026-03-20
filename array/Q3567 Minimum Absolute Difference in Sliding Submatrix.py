# array - medium
from typing import List
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:

        fmin = lambda a, b: a if a < b else b
        m, n = len(grid), len(grid[0])

        ans = [ [float('inf')] * (n-k+1) for _ in range(m-k+1) ]
        for r in range(m-k+1):
            for c in range(n-k+1):

                subgrid = set()
                for nr in range(r, r+k):
                    for nc in range(c, c+k):
                        subgrid.add(grid[nr][nc])

                subgrid = sorted(subgrid)
                # find min. diff
                if len(subgrid) == 1:
                    ans[r][c] = 0
                    continue
                
                for i in range(1, len(subgrid)):
                    ans[r][c] = fmin(ans[r][c], subgrid[i] - subgrid[i-1])

        return ans

grid, k = [[1,8],[3,-2]], 2
grid, k = [[3,-1]], 1
grid, k = [[1,-2,3],[2,3,5]], 2
grid, k = [[0,0],[0,0]], 1

Solution().minAbsDiff(grid, k)