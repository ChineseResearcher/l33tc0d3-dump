# dp - hard
from typing import List
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # dp[0][i] refers to maximum sum of strictly increasing seq. ending at i
        # dp[1][i] refers to max. sum of duonic seq. ending at i
        # dp[2][i] refers to max. sum of trionic seq. ending at i 
        dp = [ [float('-inf')] * n for _ in range(3) ]

        ans = float('-inf')
        for i in range(1, n):

            if nums[i] == nums[i-1]:
                continue

            # case 1: strictly increasing
            if nums[i] > nums[i-1]:

                # update dp[0][i]
                dp[0][i] = fmax(dp[0][i], dp[0][i-1] + nums[i])
                dp[0][i] = fmax(dp[0][i], nums[i-1] + nums[i])

                # update dp[2][i]
                # sub case 1: inherit from duonic seq.
                if dp[1][i-1] > float('-inf'):
                    dp[2][i] = fmax(dp[2][i], dp[1][i-1] + nums[i])
                # sub case 2: inherit from ongoing trionic seq.
                if dp[2][i-1] > float('-inf'):
                    dp[2][i] = fmax(dp[2][i], dp[2][i-1] + nums[i])

            # case 2: strictly decreasing
            else:

                # sub case 1: inherit from monoAsc seq.
                if dp[0][i-1] > float('-inf'):
                    dp[1][i] = fmax(dp[1][i], dp[0][i-1] + nums[i])
                # sub case 2: inherit from ongoing duonic seq.
                if dp[1][i-1] > float('-inf'):
                    dp[1][i] = fmax(dp[1][i], dp[1][i-1] + nums[i])

            ans = fmax(ans, dp[2][i])

        return ans
    
nums = [1,4,2,7]
nums = [0,-2,-1,-3,0,2,-1]
nums = [-754,167,-172,202,735,-941,992]

Solution().maxSumTrionic(nums)