# dp - hard
class Solution:
    def recursive_play(self, i, j):

        if i == self.m-1 and j == self.n-1:
            return min(self.dungeon[i][j], 0)
        
        if (i,j) in self.dp: return self.dp[(i,j)]
        
        # op1: move right
        right = self.recursive_play(i, j+1) if j+1 < self.n else float('-inf')
        # op2: move down
        down = self.recursive_play(i+1, j) if i+1 < self.m else float('-inf')

        # first we need to pick the next move that would result in 
        # lower dip in health, and second if the curr cell has a power-up
        # large enough to negate any health dip, the curr. dip in health is thus 0
        currAns = min(self.dungeon[i][j] + max(right, down), 0)
        self.dp[(i,j)] = currAns
        return currAns

    def calculateMinimumHP(self, dungeon):
        self.m, self.n, self.dungeon = len(dungeon), len(dungeon[0]), dungeon
        self.dp = dict()

        # edge case: if there's only one cell, that is we are at princess' location already
        if self.m == 1 and self.n == 1: return abs(min(self.dungeon[0][0], 0)) + 1

        return abs(self.recursive_play(0, 0)) + 1
    
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon = [[1,1,1],[1,1,1]]
dungeon = [[-3, 5]]

Solution().calculateMinimumHP(dungeon)