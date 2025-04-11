# dp - medium
from collections import defaultdict
class Solution:
    def countPathsWithXorValue(self, grid, k):
        
        m, n = len(grid), len(grid[0])
        dp = [ [defaultdict(int) for _ in range(n)] for _ in range(m)]

        startVal = grid[0][0]
        dp[0][0][startVal] = 1

        # init. the first row traversal
        for c in range(1, n):
            for xor, freq in dp[0][c-1].items():
                dp[0][c][xor ^ grid[0][c]] += freq

        for r in range(1, m):
            for xor, freq in dp[r-1][0].items():
                dp[r][0][xor ^ grid[r][0]] += freq

        MOD = int(1e9 + 7)
        for r in range(1, m):
            for c in range(1, n):

                # source 1: inherit from left cell
                for xor, freq in dp[r][c-1].items():
                    curr_k = xor ^ grid[r][c]
                    dp[r][c][curr_k] += freq
                    dp[r][c][curr_k] %= MOD

                # source 2: inherit from above cell
                for xor, freq in dp[r-1][c].items():
                    curr_k = xor ^ grid[r][c]
                    dp[r][c][curr_k] += freq
                    dp[r][c][curr_k] %= MOD

        return dp[m-1][n-1][k]
    
grid, k = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], 11
grid, k = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], 2
grid, k = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], 10

Solution().countPathsWithXorValue(grid, k)