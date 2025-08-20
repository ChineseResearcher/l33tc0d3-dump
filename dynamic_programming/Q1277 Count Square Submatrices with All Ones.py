# dp - medium
class Solution:
    def countSquares(self, matrix):
        
        # key is to figure out the inheritance relationship of dp[i][j] and its neighbouring states
        n = len(matrix)
        m = len(matrix[0]) if matrix else 0

        dp = [[0]* m for _ in range(n)]

        # initiate our ans
        ans = 0
        # fill the first row with matrix values
        for j in range(m):
            dp[0][j] = matrix[0][j]
            ans += dp[0][j]

        # fill the first column with matrix values
        for i in range(n):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]

        # if matrix[0][0] is 1 we offset our initiated ans by -1
        ans -= dp[0][0]

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1+ min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                else:
                    dp[i][j] = 0

                ans += dp[i][j]

        return ans
    
matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

Solution().countSquares(matrix)