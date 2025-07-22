# dp - medium
from typing import List
import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # core idea: iterative DP + heap (for choosing best transition)
        dp = [float('-inf')] * n

        # we are standing at index 0
        dp[0] = nums[0]

        # init. maxheap
        maxheap = [[-dp[0], 0]] # < -ve of dp[i], index>

        for i in range(1, n):

            # lazy-delete
            while maxheap and maxheap[0][1] < i - k:
                heapq.heappop(maxheap)

            dp[i] = -maxheap[0][0] + nums[i]
            # update heap
            heapq.heappush(maxheap, [-dp[i], i])

        return dp[-1]
    
nums, k = [1,-1,-2,4,-7,3], 2
nums, k = [10,-5,-2,4,0,3], 3
nums, k = [1,-5,-20,4,-1,3,-6,-3], 2

Solution().maxResult(nums, k)