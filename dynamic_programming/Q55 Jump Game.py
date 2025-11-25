# dp - medium
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        # key ideas:
        # 1) dp[i] records the farthest index that we could reach by
        # utilising all numbers in range [0...i]
        # 2) if at any dp[i], dp[i] < i, then we can early return false
        dp = [-1] * n
        dp[0] = nums[0]

        ans = True
        for i in range(1, n):

            if dp[i-1] >= i:
                curr = i + nums[i]
                prev = dp[i-1]
                
                dp[i] = max(prev, curr)

            else:
                ans = False
                break

        return ans

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [1] * int(1e4)

Solution().canJump(nums)