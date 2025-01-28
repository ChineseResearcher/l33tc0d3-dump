# graph - medium
class Solution:
    def dfs(self, r,c):

        # mark visited
        self.visited.add((r,c))

        fish = self.grid[r][c]
        # move to cardinal directions
        if c-1 >= 0 and (r, c-1) not in self.visited and self.grid[r][c-1] > 0:
            fish += self.dfs(r, c-1)
        if c+1 < self.n and (r, c+1) not in self.visited and self.grid[r][c+1] > 0:
            fish += self.dfs(r, c+1)
        if r-1 >= 0 and (r-1, c) not in self.visited and self.grid[r-1][c] > 0:
            fish += self.dfs(r-1, c)
        if r+1 < self.m and (r+1, c) not in self.visited and self.grid[r+1][c] > 0:
            fish += self.dfs(r+1, c)

        return fish

    def findMaxFish(self, grid) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid

        self.visited = set()

        ans = 0 # case if no water cell exists
        for r in range(self.m):
            for c in range(self.n):

                if self.grid[r][c] > 0 and (r,c) not in self.visited:
                    ans = max(ans, self.dfs(r,c))

        return ans
    
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]

Solution().findMaxFish(grid)