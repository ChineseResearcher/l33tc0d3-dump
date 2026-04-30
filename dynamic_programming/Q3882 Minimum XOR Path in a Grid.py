# dp - medium
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) since m x n <= 1000, and there are maximally 1023 possible 
        # intermediate XOR values, O(mnk) is feasible
        # 2) dp[i][j] stores a set of possible XOR values by traversing up to (i,j)

        dp = [ [set() for _ in range(n)] for _ in range(m) ]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):

                if i - 1 >= 0:
                    for x in dp[i-1][j]:
                        dp[i][j].add(x ^ grid[i][j])
                if j - 1 >= 0:
                    for x in dp[i][j-1]:
                        dp[i][j].add(x ^ grid[i][j])

        return min(dp[-1][-1])

grid = [[2,7,5]]
grid = [[1,2],[3,4]]
grid = [[6,7],[5,8]]
grid = [[5,28,28,15],[5,11,17,17]]
grid = [[10,4,15,7],[9,24,19,22]]

Solution().minCost(grid)