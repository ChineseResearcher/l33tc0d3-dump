# dp - medium
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1: return nums[0]
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) because the houses are now arranged in a circle,
        # so the starting point can be anywhere in the circle, and that the last 
        # house before the first picked house will not be considered
        # 2) it suffices to consider 2 cases:
        # - robbing first n - 1 houses
        # - robbing last n - 1 houses

        def solve(arr:List[int]) -> int:

            dp, ans = [0] * (n - 1), arr[0]
            for i in range(n - 1):

                dp[i] += arr[i]
                prevMax = 0
                if i > 1:
                    for j in range(i - 1):
                        prevMax = fmax(prevMax, dp[j])
                dp[i] += prevMax
                ans = fmax(ans, dp[i])

            return ans

        op1, op2 = solve(nums[:-1]), solve(nums[1:])
        return fmax(op1, op2)

nums = [2,3,2]
nums = [1,2,3]
nums = [1,2,3,1]

Solution().rob(nums)