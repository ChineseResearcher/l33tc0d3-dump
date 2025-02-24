# simulation - medium
class Solution:
    def countUnguarded(self, m, n, guards, walls):
        isWall = [[False] * n for _ in range(m)] 
        isGuard = [[False] * n for _ in range(m)] 
        monitored = [[False] * n for _ in range(m)]
        monitored_cnt = 0

        for w in walls:
            isWall[w[0]][w[1]] = True
            # let any wall be True so that only the unmonitored are False
            monitored[w[0]][w[1]] = True 

        for g in guards:
            isGuard[g[0]][g[1]] = True

        for g in guards:

            currRow, currCol = g[0], g[1]
            monitored[currRow][currCol] = True
            # check east
            for col in range(currCol+1, n):
                if isWall[currRow][col] or isGuard[currRow][col]:
                    break
                monitored[currRow][col] = True

            # check west
            for col in range(currCol-1, -1, -1):
                if isWall[currRow][col] or isGuard[currRow][col]:
                    break
                monitored[currRow][col] = True

            # check south
            for row in range(currRow+1, m):
                if isWall[row][currCol] or isGuard[row][currCol]:
                    break
                monitored[row][currCol] = True

            # check north
            for row in range(currRow-1, -1, -1):
                if isWall[row][currCol] or isGuard[row][currCol]:
                    break
                monitored[row][currCol] = True

        return m * n - sum([sum(row) for row in monitored])
    
m, n, guards, walls = 4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]
m, n, guards, walls = 3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]

Solution().countUnguarded(m, n, guards, walls)