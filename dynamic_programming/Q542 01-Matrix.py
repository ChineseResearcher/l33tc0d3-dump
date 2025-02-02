# dp - medium
from collections import deque
class Solution:
    def updateMatrix(self, mat):
        
        m, n = len(mat), len(mat[0])

        # initiate a 2-D dp storing the distance to nearest 0 at mat[i][j]
        # at the same time enqueue any 0-cells for BFS later
        dp = [[float('inf')] * n for _ in range(m)]
        bfs_queue = deque([])
        visited = set()

        for i in range(m):
            for j in range(n):

                if mat[i][j] == 0:
                    dp[i][j] = 0
                    bfs_queue.append([i,j])
                    visited.add((i, j))

        while bfs_queue:

            row, col = bfs_queue.popleft()
            # update dp only when it is 1
            if mat[row][col] == 1:

                curr_ans = float('inf')
                # if a 1-cell is surrounded by some other 1-cells, and that the
                # 1-cell with the smallest dp val. = 2, then it takes 2+1 = 3
                # units of distance to reach to the nearest 0-cell

                # left
                if col-1 >= 0: curr_ans = min(curr_ans, dp[row][col-1]+1)
                # right
                if col+1 < n: curr_ans = min(curr_ans, dp[row][col+1]+1)
                # down
                if row+1 < m: curr_ans = min(curr_ans, dp[row+1][col]+1)
                # up
                if row-1 >= 0: curr_ans = min(curr_ans, dp[row-1][col]+1)

                dp[row][col] = curr_ans

            # update bfs_queue
            if col-1 >= 0 and (row, col-1) not in visited:
                bfs_queue.append([row, col-1])
                visited.add((row, col-1))
            if col+1 < n and (row, col+1) not in visited:
                bfs_queue.append([row, col+1])
                visited.add((row, col+1))
            if row-1 >= 0 and (row-1, col) not in visited:
                bfs_queue.append([row-1, col])
                visited.add((row-1, col))
            if row+1 < m and (row+1, col) not in visited:
                bfs_queue.append([row+1, col])
                visited.add((row+1, col))

        return dp
    
mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[1,1,1],[0,1,1],[1,1,1]]

Solution().updateMatrix(mat)