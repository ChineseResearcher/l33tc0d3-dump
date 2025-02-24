# simulation - medium
class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])

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

        # our spiral seq.
        ans = []
        while True:

            # seq. fully loaded
            if len(ans) == m * n:
                break

            ans.append(matrix[r][c])
            # mark visited
            visited.add((r,c))

            # change direction if:
            # we are at corner cells OR
            # the next cell in the currDir has been visited
            nr, nc = r+increments[currDir][0], c+increments[currDir][1]
            if (nr < 0 or nr >= m or nc < 0 or nc >= n) or (nr, nc) in visited:
                currDir = (currDir + 1) % 4

            r += increments[currDir][0]
            c += increments[currDir][1]

        return ans
    
matrix = [[2,3]]
matrix = [[2],[3]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Solution().spiralOrder(matrix)