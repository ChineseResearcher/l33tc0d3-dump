# dp - hard
class Solution:
    # why the two-dfs idea works is because in the original question,
    # the two-leg trips: (0,0) -> (n-1,n-1); (n-1,n-1) -> (0,0)
    # would result in second trip being dependent on what has been picked
    # in the first trip, thus by running two-dfs side-by-side we avoid
    # the possibility of re-picking cherries at the same locations
    def recursive_pick(self, i, j, p):

        # we have two robots moving simultaneously from (0,0)
        # to (n-1, n-1), each making independent decisions
        if i == self.n-1 and j == self.n-1 and p == self.n-1:
            return 1 if self.grid[i][j] == 1 else 0

        # the space optimisation trick to reduce dimensions from
        # (i,j,p,q) where (i,j) denotes the first robot and (p,q)
        # denotes the second robot, is to encode q as i+j-p
        q = i + j - p

        if (i,j,p) in self.dp: return self.dp[(i,j,p)]

        # there are in total four combinations possible:
        currAns = float('-inf')
        # 1) r1 moves right & r2 moves right
        if j+1 < self.n and self.grid[i][j+1] != -1 and q+1 < self.n and self.grid[p][q+1] != -1:
            currAns = max(currAns, self.recursive_pick(i, j+1, p))
        # 2) r1 moves right & r2 moves down
        if j+1 < self.n and self.grid[i][j+1] != -1 and p+1 < self.n and self.grid[p+1][q] != -1:
            currAns = max(currAns, self.recursive_pick(i, j+1, p+1))
        # 3) r1 moves down & r2 moves down
        if i+1 < self.n and self.grid[i+1][j] != -1 and p+1 < self.n and self.grid[p+1][q] != -1:
            currAns = max(currAns, self.recursive_pick(i+1, j, p+1))
        # 4) r1 moves down & r2 moves right
        if i+1 < self.n and self.grid[i+1][j] != -1 and q+1 < self.n and self.grid[p][q+1] != -1:
            currAns = max(currAns, self.recursive_pick(i+1, j, p))

        # for the current cells that the two robots are at, we
        # consider the cherries that can be picked up
        if i == p and j == q:
            currVal = 1 if self.grid[i][j] == 1 else 0
        else:
            currVal = 0
            if self.grid[i][j] == 1: currVal += 1
            if self.grid[p][q] == 1: currVal += 1

        currAns += currVal
        self.dp[(i,j,p)] = currAns
        return currAns

    def cherryPickup(self, grid):
        self.dp = dict()
        self.n, self.grid = len(grid), grid

        # egde case 1: topLeft or botRight cell not reachable
        if grid[0][0] == -1 or grid[-1][-1] == -1: return 0

        # edge case 2: smallest square
        if self.n == 1: return 1 if grid[0][0] == 1 else 0

        # the question desires a return to (0,0) as the final end-point
        # however, we could also use two simultaneous dfs to go from (0,0) to (n-1, n-1) only
        # it is guaranteed that such a simulation would pick up the max. number of cherries
        return max(self.recursive_pick(0,0,0), 0)
    
grid = [[0,1,-1],
        [1,0,-1],
        [1,1,1]]

grid = [[1,1,-1],
        [1,-1,1],
        [-1,1,1]]

grid = [[1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,1],
        [1,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,1,1,1]]

Solution().cherryPickup(grid)