# dp - medium
from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)
        # core ideas:
        # 1) construct a 2 x n DP matrix, w/ row 0 indicating -ve, row 1 +ve
        # 2) depending on whether nums[i] is +ve or -ve, extend the max. length of subarr.
        # w/ +ve / -ve product by looking at dp[i-1]
        dp = [ [0] * n for _ in range(2) ]

        # init. vals for first index
        if nums[0] > 0:
            dp[1][0] = 1
        elif nums[0] < 0:
            dp[0][0] = 1

        ans = dp[1][0]
        for i in range(1, n):

            if nums[i] > 0:

                # extend +ve subarr using prev +ve subarr
                dp[1][i] = dp[1][i-1] + 1
                # extend -ve subarr using prev -ve subarr
                # provided that prev -ve subarr exists
                if dp[0][i-1] > 0:
                    dp[0][i] = dp[0][i-1] + 1
                
            if nums[i] < 0:

                # extend -ve subarr using prev +ve subarr
                dp[0][i] = dp[1][i-1] + 1
                # extend +ve subarr using prev -ve subarr
                # provided that prev -ve subarr exists
                if dp[0][i-1] > 0:
                    dp[1][i] = dp[0][i-1] + 1
                
            ans = max(ans, dp[1][i])

        return ans
    
nums = [1,-2,-3,4]
nums = [0,1,-2,-3,-4]
nums = [-1,-2,-3,0,1]
nums = [-16,0,-5,2,2,-13,11,8]

Solution().getMaxLen(nums)