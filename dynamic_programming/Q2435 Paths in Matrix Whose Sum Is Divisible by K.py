# dp - hard
from typing import List
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])

        dp = [ [ [0] * k for _ in range(n) ] for _ in range(m) ]
        dp[-1][-1][grid[-1][-1] % k] += 1

        MOD = int(1e9 + 7)
        # inverse traversal from (m-1, n-1) to (0, 0)
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):

                curr = grid[r][c] % k
                # right-cell inherit
                if c + 1 < n:

                    for remainder in range(k):
                        new_rem = (curr + remainder) % k
                        dp[r][c][new_rem] += dp[r][c+1][remainder]
                        dp[r][c][new_rem] %= MOD

                # bottom-cell inherit
                if r + 1 < m:

                    for remainder in range(k):
                        new_rem = (curr + remainder) % k
                        dp[r][c][new_rem] += dp[r+1][c][remainder]
                        dp[r][c][new_rem] %= MOD
        
        return dp[0][0][0] # remainder = 0 is our answer

grid, k = [[5,2,4],[3,0,5],[0,7,2]], 3
grid, k = [[0,0]], 5
grid, k = [[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1

Solution().numberOfPaths(grid, k)