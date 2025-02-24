# simulation - medium
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        # how do we simulate the spiral moves ?
        # clockwise movement with regular increments in the max. distance travelled in a given direction
        travelled_grid = [[rStart, cStart]]
        hits = 0 # this iterator controls our max. distance and direction
        currRow, currCol = rStart, cStart

        # exit condition: we have traversed all possible grids
        while len(travelled_grid) < rows * cols:
            max_distance = hits // 2 + 1
            direction = hits % 4 # ranges between [0, 3] for right, down, left, up respectively

            # Note: currRow & currCol gets updated when we exhaust the max_distance in a given direction
            # move right
            if direction == 0: 
                for i in range(1, max_distance + 1):
                    if 0 <= currRow < rows and 0 <= currCol + i < cols:
                        travelled_grid.append([currRow, currCol + i])
                currCol = currCol + i
                
            # move down
            elif direction == 1:
                for i in range(1, max_distance + 1):
                    if 0 <= currRow + i < rows and 0 <= currCol < cols:
                        travelled_grid.append([currRow + i, currCol])
                currRow = currRow + i

            # move left
            elif direction == 2:
                for i in range(1, max_distance + 1):
                    if 0 <= currRow < rows and 0 <= currCol - i < cols:
                        travelled_grid.append([currRow, currCol - i])
                currCol = currCol - i

            # move up
            elif direction == 3:
                for i in range(1, max_distance + 1):
                    if 0 <= currRow - i < rows and 0 <= currCol < cols:
                        travelled_grid.append([currRow - i, currCol])
                currRow = currRow - i

            hits += 1
        
        return travelled_grid
    
rows, cols, rStart, cStart = 5, 6, 1, 4
rows, cols, rStart, cStart = 1, 4, 0, 0

Solution().spiralMatrixIII(rows, cols, rStart, cStart)