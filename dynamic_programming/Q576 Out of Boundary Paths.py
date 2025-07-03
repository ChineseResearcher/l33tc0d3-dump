# dp - medium
class Solution:
    def dfs_path(self, moves, row, col): 
        
        # if we found the boundary, return 1
        if row < 0 or row >= self.m or col < 0 or col >= self.n:
            return 1
        # if we have exhausted our moves, return 0
        if moves == 0:
            return 0
        
        # return memoization result
        if self.dp[moves][row][col] != -1:
            return self.dp[moves][row][col]
        
        # further dfs in cardinal directions
        obp = 0
        obp += self.dfs_path(moves - 1, row + 1, col)
        obp += self.dfs_path(moves - 1, row - 1, col)
        obp += self.dfs_path(moves - 1, row, col + 1)
        obp += self.dfs_path(moves - 1, row, col - 1)
        
        # memoization
        self.dp[moves][row][col] = int(obp % (1e9 + 7))
        
        return obp

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        self.m, self.n = m, n

        # initialize a 3D dp array to store results for each (moves, row, col) combination
        self.dp = [[[-1] * self.n for _ in range(self.m)] for _ in range(maxMove + 1)]

        return int(self.dfs_path(maxMove, startRow, startColumn) % (1e9 + 7))
    
m, n, maxMove, startRow, startColumn = 2, 2, 2, 0, 0
m, n, maxMove, startRow, startColumn = 1, 3, 3, 0, 1
m, n, maxMove, startRow, startColumn = 8, 50, 23, 5, 26
m, n, maxMove, startRow, startColumn = 36, 5, 50, 15, 3
m, n, maxMove, startRow, startColumn = 10, 10, 0, 5, 5

Solution().findPaths(m, n, maxMove, startRow, startColumn)