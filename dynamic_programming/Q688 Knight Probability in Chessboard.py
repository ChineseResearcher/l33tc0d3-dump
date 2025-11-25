# dp - medium
class Solution:
    def dp_ones_initiate(self, dp_2d):
        
        # initiate negative ones to the double-layer padding
        # and we do not want to inherit from dp cells where dp[i][j] == -1
        for col in range(len(dp_2d[0])):
            dp_2d[0][col], dp_2d[1][col] = -1, -1
            dp_2d[-1][col], dp_2d[-2][col] = -1, -1
            
        for row in range(len(dp_2d)):
            dp_2d[row][0], dp_2d[row][1] = -1, -1
            dp_2d[row][-1], dp_2d[row][-2] = -1, -1
            
        return dp_2d

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # code structure similar to LC Out of Boundary Paths
        maxMove = k
        n, m = n, n
        startRow, startColumn = row, column

        # edge case: no move allowed, definitely stay on board
        if maxMove == 0:
            return 1

        # wrap a double-layer padding around the original mxn matrix
        obp_prev = [[1] * (n+4)  for _ in range(m+4)]
        obp_prev = self.dp_ones_initiate(obp_prev)

        for _ in range(maxMove):
            
            obp_curr = [[1] * (n+4)  for _ in range(m+4)]
            obp_curr = self.dp_ones_initiate(obp_curr)
            
            for row in range(2, m+2):
                for col in range(2, n+2):
                    
                    # transition from prev_move state
                    # each storing the number of unique in-the-boundary paths passing through it after k moves
                    obp_curr[row][col] = (max(obp_prev[row-1][col-2], 0) + \
                                          max(obp_prev[row-2][col-1], 0) + \
                                          max(obp_prev[row-2][col+1], 0) + \
                                          max(obp_prev[row-1][col+2], 0) + \
                                          max(obp_prev[row+1][col+2], 0) + \
                                          max(obp_prev[row+2][col+1], 0) + \
                                          max(obp_prev[row+2][col-1], 0) + \
                                          max(obp_prev[row+1][col-2], 0))
                    
            # overwrite prev_dp w/ curr_dp
            obp_prev = obp_curr

        # adjust querying indices as we've padded our dp matrix
        return obp_curr[startRow+2][startColumn+2] / (8 ** maxMove)

n, k, row, column = 3, 2, 0, 0
n, k, row, column = 1, 0, 0, 0
n, k, row, column = 1, 1, 0, 0
n, k, row, column = 3, 3, 0, 0
# constraint
n, k, row, column = 25, 100, 0, 0

Solution().knightProbability(n, k, row, column)