# simulation - medium
class Solution:
    def findBall(self, grid):

        m, n = len(grid), len(grid[0])
        # we place a ball onto each column and simulate if it falls through
        ans = []
        for col in range(n):

            row = 0
            while True:

                if row == m:
                    ans.append(col)
                    break

                # if we face onto a cell with "\" (1)
                # check boundary condition by looking at the right cell, vice versa
                curr = grid[row][col]

                if curr == 1:

                    # wall adjacent cell & wall facing board results in blockage directly
                    if col+1 > n-1 or grid[row][col+1] == -1: 
                        ans.append(-1)
                        break
                    row += 1
                    col += 1

                elif curr == -1:

                    if col-1 < 0 or grid[row][col-1] == 1:
                        ans.append(-1)
                        break
                    row += 1
                    col -= 1
                
        return ans
    
grid = [[-1]]
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

Solution().findBall(grid)