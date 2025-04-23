# graph - medium
from collections import deque
class Solution:
    def numIslands(self, grid):
        
        m, n = len(grid), len(grid[0])
        # maintain a set storing visited "1"s at the global level
        global_visited = set()

        islandCnt = 0
        for r in range(m):
            for c in range(n):
                
                if grid[r][c] == '1' and (r,c) not in global_visited:
                    islandCnt += 1
                    global_visited.add((r,c))
                    # start a bfs traversal
                    visited, bfs_queue = set(((r,c),)), deque([(r,c)])
                    
                    while bfs_queue:
                        row, col = bfs_queue.popleft()
                        # check cardinal
                        if row + 1 < m and (row+1, col) not in visited and grid[row+1][col] == '1':
                            bfs_queue.append((row+1, col))
                            visited.add((row+1, col))
                            global_visited.add((row+1, col))
                            
                        if row - 1 >= 0 and (row-1, col) not in visited and grid[row-1][col] == '1':
                            bfs_queue.append((row-1, col))
                            visited.add((row-1, col))
                            global_visited.add((row-1, col))
                            
                        if col + 1 < n and (row, col+1) not in visited and grid[row][col+1] == '1':
                            bfs_queue.append((row, col+1))
                            visited.add((row, col+1))
                            global_visited.add((row, col+1))
                        
                        if col - 1 >= 0 and (row, col-1) not in visited and grid[row][col-1] == '1':
                            bfs_queue.append((row, col-1))
                            visited.add((row, col-1))
                            global_visited.add((row, col-1))
                            
        return islandCnt
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Solution().numIslands(grid)