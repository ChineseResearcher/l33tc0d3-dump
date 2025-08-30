# dp - medium
class Solution:
    def minFallingPathSum(self, matrix) -> int:

        m, n = len(matrix), len(matrix[0])

        # matrix is treated as the dp grid directly
        for i in range(1, m):

            for j in range(n):

                # inherit from top-left
                op1 = matrix[i-1][j-1] if j-1 >= 0 else float('inf')

                # inherit from above
                op2 = matrix[i-1][j]

                # inherit from top-right
                op3 = matrix[i-1][j+1] if j+1 < n else float('inf')

                matrix[i][j] += min(op1, min(op2, op3))

        return min(matrix[-1])
    
matrix = [[2,1,3],[6,5,4],[7,8,9]]
matrix = [[-19,57],[-40,-5]]

Solution().minFallingPathSum(matrix)