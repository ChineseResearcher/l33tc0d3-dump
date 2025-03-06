# array - easy
class Solution:
    def findMissingAndRepeatedValues(self, grid):
        
        # our 2-D grid is of dimension n x n
        n = len(grid)

        # maintain a seen set
        seen = set()

        # sum of 1 to n^2 can be precomputed
        expectedSum = int((1 + n**2) * n**2 / 2)

        a, b = None, None
        for i in range(n):
            for j in range(n):

                if grid[i][j] in seen:
                    a = grid[i][j]
                    continue

                expectedSum -= grid[i][j]
                seen.add(grid[i][j])

        b = expectedSum
        return [a, b]
    
grid = [[1,3],[2,2]]
grid = [[9,1,7],[8,9,2],[3,4,6]]

Solution().findMissingAndRepeatedValues(grid)