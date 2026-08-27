# dp - medium
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) linear DP
        # 2) transition from all dp[j] where j < i - 1 so as to 
        # satisfy non-adjacency as required by the question

        dp, ans = [0] * n, 0
        for i in range(n):

            dp[i] += nums[i]
            prevMax = 0
            if i > 1:
                for j in range(i - 1):
                    prevMax = fmax(prevMax, dp[j])
            dp[i] += prevMax
            ans = fmax(ans, dp[i])

        return ans

nums = [1,2,3,1]
nums = [2,7,9,3,1]

Solution().rob(nums)