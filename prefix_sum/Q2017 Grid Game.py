# prefix sum - medium
class Solution:
    def gridGame(self, grid) -> int:
        n = len(grid[0])
        # intiate pf_sum for each of the two rows
        pf_sum1, pf_sum2 = [], []

        currSum1, currSum2 = 0, 0
        for i in range(n):
            currSum1 += grid[0][i]
            pf_sum1.append(currSum1)

            currSum2 += grid[1][i]
            pf_sum2.append(currSum2)

        # at each iterated idx, compare the pf_sum for two rows
        # as all players are only allowed to move down/right
        # strategically find a point where player 1 should turn down
        currRow, currCol = 0, 0
        while True:

            # if we are at last col, we have to turn down
            if currCol == n-1: 
                grid[currRow][currCol] = 0
                currRow = min(1, currRow+1)

            # for cells covered by player 1's path, reset to 0
            grid[currRow][currCol] = 0

            # exit when we reached (1, n-1) cell
            if currCol == n-1 and currRow == 1:
                break

            # we are only heading right if currRow == 1 already
            if currRow == 0:
                
                # core decision: player 1 wants to minimise the max. points player 2
                # can get, so he/she would want to always compare between
                # 1) row1 sum from currCol onwards
                # 2) row2 sum up to currCol
                curr_row_sum = pf_sum1[n-1] - pf_sum1[currCol]
                next_row_sum = pf_sum2[currCol]
                
                if next_row_sum > curr_row_sum:
                    currRow += 1
                else:
                    currCol += 1

            elif currRow == 1: currCol += 1 

        # as for the max. points earnable by player 2, just look at 
        # which row sum is bigger and that is the solution
        return max(sum(grid[0]), sum(grid[1]))
    
grid = [[2,5,4],[1,5,1]]
grid = [[3,3,1],[8,5,2]]
grid = [[1,3,1,15],[1,3,3,1]]
grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]

Solution().gridGame(grid)