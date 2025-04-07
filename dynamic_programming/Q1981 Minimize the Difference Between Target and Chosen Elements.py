# dp - medium
class Solution:
    def recursive_pick(self, r, currSum):

        if r == self.m:
            return abs(currSum - self.target)
        
        if (r, currSum) in self.dp: return self.dp[(r, currSum)]

        currAns = float('inf')
        # pruning: when currSum already exceeds target
        # we shall just use the min. of curr row
        if currSum >= self.target or currSum + self.rowMin[r] >= self.target:
            currAns = self.recursive_pick(r+1, currSum + self.rowMin[r])
        else:
            # explore all possible cells in a row
            for c in range(self.n):
                currAns = min(currAns, self.recursive_pick(r+1, currSum + self.mat[r][c]))

        self.dp[(r, currSum)] = currAns
        return currAns

    def minimizeTheDifference(self, mat, target):
        self.m, self.n = len(mat), len(mat[0])
        self.mat = mat
        self.target = target

        self.rowMin = {r: min(self.mat[r]) for r in range(self.m)}

        self.dp = dict()
        return self.recursive_pick(0, 0)
    
mat, target = [[1,2,3],[4,5,6],[7,8,9]], 13
mat, target = [[1],[2],[3]], 100
mat, target = [[1,2,9,8,7]], 6

Solution().minimizeTheDifference(mat, target)