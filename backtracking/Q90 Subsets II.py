# backtracking - medium
class Solution:
    def backtrack(self, startIdx, comb):

        if startIdx == self.n+1:
            return
        
        self.ans.add(tuple(sorted(comb)))
        for i in range(startIdx, self.n):
            comb.append(self.nums[i])
            self.backtrack(i+1, comb)
            comb.pop() # roll back

    def subsetsWithDup(self, nums):
        self.n = len(nums)
        self.nums = nums

        self.ans = set()

        self.backtrack(0, [])
        return [list(x) for x in self.ans]
    
nums = [1,2,2]
nums = [0]
nums = [4,4,4,1,4]

Solution().subsetsWithDup(nums)