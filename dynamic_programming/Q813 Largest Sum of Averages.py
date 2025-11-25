# dp - medium
from typing import List
class Solution:
    def recursiveGrouping(self, startIdx, groupedCnt, score):

        if groupedCnt == self.k:
            score += sum(self.nums[startIdx:]) / (self.n-startIdx)
            self.ans = max(self.ans, score)
            return
        
        if score < self.dp[startIdx][groupedCnt-1]:
            return
        
        self.dp[startIdx][groupedCnt-1] = max(self.dp[startIdx][groupedCnt-1], score)
        
        running_sum = 0
        for i in range(startIdx, self.n-(self.k-groupedCnt)):
            running_sum += self.nums[i]
            self.recursiveGrouping(i+1, groupedCnt+1, score + running_sum / (i-startIdx+1))

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        self.n, self.k = len(nums), k
        self.nums = nums

        self.ans = 0
        # our memorization is a 2D matrix storing the result to a subproblem
        # largest sum of averages if we are looking at nums[:(i+1)] and groups of j
        self.dp = [[0] * self.k for _ in range(self.n)]

        self.recursiveGrouping(0, 1, 0)

        return self.ans

nums, k = [9,1,2,3,9], 3
nums, k = [1,2,3,4,5,6,7], 4
nums, k = [4,1,7,5,6,2,3], 4

Solution().largestSumOfAverages(nums, k)