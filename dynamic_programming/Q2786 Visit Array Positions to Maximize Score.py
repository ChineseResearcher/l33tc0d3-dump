# dp - medium
from typing import List
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        # init. dp arr. of length n
        dp = [float('-inf')] * n
        dp[0] = nums[0] # as per qn, init. points = nums[0]

        # keep track of the last odd/even nums[i]
        # one thing to note is that we are constrained to be starting from index 0
        odd_max, even_max, ans = float('-inf'), float('-inf'), 0
        for i in range(n):

            # curr. is even
            if nums[i] % 2 == 0:

                if even_max > float('-inf'):
                    dp[i] = max(dp[i], even_max + nums[i])
                if odd_max > float('-inf'):
                    dp[i] = max(dp[i], odd_max + nums[i] - x)

                even_max = max(even_max, dp[i])

            # curr. is odd
            else:

                if even_max > float('-inf'):
                    dp[i] = max(dp[i], even_max + nums[i] - x)
                if odd_max > float('-inf'):
                    dp[i] = max(dp[i], odd_max + nums[i])

                odd_max = max(odd_max, dp[i])

            ans = max(ans, dp[i])

        return ans
    
nums, x = [2,3,6,1,9,2], 5
nums, x = [2,4,6,8], 3
nums, x = [8,50,65,85,8,73,55,50,29,95,5,68,52,79], 74
nums, x = [9,58,17,54,91,90,32,6,13,67,24,80,8,56,29,66,85,38,45,13,20,73,16,98,28,56,23,2,47,85,11,97,72,2,28,52,33], 90

Solution().maxScore(nums, x)