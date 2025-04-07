# dp - medium
class Solution:
    def recursivePartition(self, idx, cumuSum):
        # terminal condition
        if idx == self.n:
            return cumuSum == self.totalSum // 2

        # use memoized result
        if (idx, cumuSum) in self.dp:
            return self.dp[(idx, cumuSum)]

        currAns = False
        take = self.recursivePartition(idx+1, cumuSum + self.nums[idx])
        skip = self.recursivePartition(idx+1, cumuSum)

        currAns = (currAns or (take or skip))

        # memoization
        self.dp[(idx, cumuSum)] = currAns
        return currAns

    def canPartition(self, nums) -> bool:
        self.n = len(nums)
        self.nums = nums
        self.totalSum = sum(self.nums) 
        # quick observation: odd sum cannot be partitioned equally
        if self.totalSum % 2 != 0:
            return False

        self.dp = dict()
        return self.recursivePartition(0, 0)

# attempted bottom-up because dfs+memo is really slow for this qn 
class Solution:
    def canPartition(self, nums) -> bool:
        # since we want two equal subsets, we can think of the problem
        # as asking if we can choose a subset of numbers that adds up to sum(nums) // 2
        totalSum = sum(nums)

        # only even totalSum would have two possible equal subset sum
        if totalSum % 2 != 0: return False
        targetNum = totalSum // 2

        n = len(nums)
        # construct a dp of size (n+1) * (targetNum + 1) denoting 
        # whether it is possible to add up to exactly j, using up to i-th numbers
        dp = [ [False] * (targetNum + 1) for _ in range(n+1)]

        # it is always possible to add to sum 0 using any numbers available
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1, n+1):
            for j in range(1, targetNum+1):
                
                # op1: skip the curr. target number j
                skip = dp[i-1][j]
                
                # op2: form the curr. target number j
                # by nums[i], and j - nums[i] out of nums[:i]
                # note: j should be >= nums[i]       
                take = dp[i-1][j-nums[i-1]] if j >= nums[i-1] else False
                
                dp[i][j] = (skip or take)
                
        return dp[n][targetNum]
    
nums = [1,5,11,5]
nums = [1,2,3,5]

Solution().canPartition(nums)