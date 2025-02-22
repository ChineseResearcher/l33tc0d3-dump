# dp - medium
class Solution:
    def maximalSquare(self, matrix):
        n, m = len(matrix), len(matrix[0])
        # initiate a 2-D dp to store the maximal square area @ (i,j)
        dp = [[None] * m for _ in range(n)]
        
        # for first row and col, fill the dp with its corresponding matrix number
        for nCol in range(m):
            dp[0][nCol] = int(matrix[0][nCol])
        
        for nRow in range(n):
            dp[nRow][0] = int(matrix[nRow][0])
        
        if '1' in [max(row) for row in matrix]:
            maximalSquareArea = 1
        else:
            return 0 # matrix is all zeroes
            
        for i in range(1, n):
            for j in range(1, m):
        
                if int(matrix[i][j]) != 0:
                    # compute minimum of the immediate left, top, top-left cell value
                    adjCellsMin = min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1]))
                    # update dp at current (i,j)
                    dp[i][j] = int((adjCellsMin ** 0.5 + int(matrix[i][j])) ** 2)
                    maximalSquareArea = max(maximalSquareArea, dp[i][j])
                else:
                    dp[i][j] = 0

        return maximalSquareArea
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"],["1","0"]]
matrix = [["0"]]
# Google farmer TC
matrix = [["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"]]

Solution().maximalSquare(matrix)