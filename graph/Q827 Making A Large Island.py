# graph - hard
from collections import deque
class Solution:
    def largestIsland(self, grid) -> int:
        n = len(grid)
        # for each land cell, assign an island id
        grouping = dict()

        # for each island, record the area
        area = {-1:0} # assign a dummy default

        newestIsland = 0
        for r in range(n):
            for c in range(n):

                if grid[r][c] == 1 and (r, c) not in grouping:
                    # initiate a bfs from this cell
                    bfs_queue = deque([[r,c]])
                    visited = set([(r,c)])

                    currArea = 1
                    while bfs_queue:

                        currR, currC = bfs_queue.popleft()
                        # assign grouping
                        grouping[(currR, currC)] = newestIsland

                        if currC - 1 >= 0 and grid[currR][currC-1] == 1 and (currR, currC-1) not in visited:
                            bfs_queue.append([currR, currC-1])
                            currArea += 1
                            visited.add((currR, currC-1))

                        if currC + 1 < n and grid[currR][currC+1] == 1 and (currR, currC+1) not in visited:
                            bfs_queue.append([currR, currC+1])
                            currArea += 1
                            visited.add((currR, currC+1))

                        if currR - 1 >= 0 and grid[currR-1][currC] == 1 and (currR-1, currC) not in visited:
                            bfs_queue.append([currR-1, currC])
                            currArea += 1
                            visited.add((currR-1, currC))

                        if currR + 1 < n and grid[currR+1][currC] == 1 and (currR+1, currC) not in visited:
                            bfs_queue.append([currR+1, currC])
                            currArea += 1
                            visited.add((currR+1, currC))

                    area[newestIsland] = currArea
                    newestIsland += 1

        ans = 0
        for r in range(n):
            for c in range(n):

                # identify all 0-cell and turn this cell 1
                if grid[r][c] == 0:
                    currAns, adjGrp = 0, set()

                    # check cardinal
                    if c-1 >= 0 and grid[r][c-1] == 1 and grouping[(r,c-1)] not in adjGrp:
                        adjGrp.add(grouping[(r,c-1)])
                        currAns += area[grouping[(r,c-1)]]

                    if c+1 < n and grid[r][c+1] == 1 and grouping[(r,c+1)] not in adjGrp:
                        adjGrp.add(grouping[(r,c+1)])
                        currAns += area[grouping[(r,c+1)]]

                    if r-1 >= 0 and grid[r-1][c] == 1 and grouping[(r-1,c)] not in adjGrp:
                        adjGrp.add(grouping[(r-1,c)])
                        currAns += area[grouping[(r-1,c)]]
                    
                    if r+1 < n and grid[r+1][c] == 1 and grouping[(r+1,c)] not in adjGrp:
                        adjGrp.add(grouping[(r+1,c)])
                        currAns += area[grouping[(r+1,c)]]

                    ans = max(ans, currAns + 1)

        return max(ans, max(area.values()))
                
grid = [[1,0],[0,1]]
grid = [[1,1,0],[1,0,1],[0,1,0]]
grid = [[1,1],[1,0]]
grid = [[1,1],[1,1]]
grid = [[0,0],[1,1]]

Solution().largestIsland(grid)