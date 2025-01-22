# graph - medium
from collections import deque
class Solution:
    def highestPeak(self, isWater):
        
        m, n = len(isWater), len(isWater[0])
        # this is a classical multisource BFS problem
        # and it's similar to LC542 01-matrix, except that no DP is needed here

        bfs_queue = deque([])
        visited = set()

        # our height assignments
        ans = [[float('inf')] * n for _ in range(m)]

        # enqueue all the water cells (0-cell) into the queue and mark visited
        for i in range(m):
            for j in range(n):

                if isWater[i][j] == 1:
                    bfs_queue.append([i, j])
                    visited.add((i, j))

                    # according to qn, water cells can only have height 0
                    ans[i][j] = 0


        while bfs_queue:

            r, c = bfs_queue.popleft()
            neighborMin = float('inf')

            # check cardinal directions for neighbouring unvisited cells
            if c-1 >= 0:
                if (r, c-1) not in visited:
                    bfs_queue.append([r, c-1])
                    visited.add((r, c-1))
                neighborMin = min(neighborMin, ans[r][c-1])

            if c+1 < n:
                if (r, c+1) not in visited:
                    bfs_queue.append([r, c+1])
                    visited.add((r, c+1))
                neighborMin = min(neighborMin, ans[r][c+1])

            if r-1 >= 0:
                if (r-1, c) not in visited:
                    bfs_queue.append([r-1, c])
                    visited.add((r-1, c))
                neighborMin = min(neighborMin, ans[r-1][c])

            if r+1 < m:
                if (r+1, c) not in visited:
                    bfs_queue.append([r+1, c])
                    visited.add((r+1, c))
                neighborMin = min(neighborMin, ans[r+1][c])

            # assign variable height if it is a land cell
            if isWater[r][c] != 1:
                ans[r][c] = neighborMin + 1

        return ans
    
isWater = [[0,1],[0,0]]
isWater = [[0,0,1],[1,0,0],[0,0,0]]

Solution().highestPeak(isWater)