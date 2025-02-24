# simulation - medium
class Solution:
    def generateMatrix(self, n):
        # initiate our 2D arr. with 0s
        ans = [[0] * n for _ in range(n)]

        # build a increment instruction dict for diff. directions
        increments = {
            0: [0, 1], # rightwards
            1: [1, 0], # downwards
            2: [0,-1], # leftwards
            3: [-1,0]  #upwards
            }

        # start from (0,0) cell, and move right
        currDir = 0
        r, c = 0, 0

        # maintain a visited
        visited = set()

        # logic similar to Spiral Matrix I except that now we fill the cell with num
        num = 1
        while True:

            # we have filled numbers 1 - n^2
            if num > n ** 2:
                break
            
            # fill number in spiral form
            ans[r][c] = num
            num += 1

            # mark visited
            visited.add((r,c))

            # change direction if:
            # we are at corner cells OR
            # the next cell in the currDir has been visited
            nr, nc = r+increments[currDir][0], c+increments[currDir][1]
            if (nr < 0 or nr >= n or nc < 0 or nc >= n) or (nr, nc) in visited:
                currDir = (currDir + 1) % 4

            r += increments[currDir][0]
            c += increments[currDir][1]

        return ans
    
n = 3
n = 1

Solution().generateMatrix(n)