# dp - medium
from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # we could use dp to find the Longest Non-Decreasing Subsequence
        # which would in turn imply the min. deletions needed as the answer
        dp = [1] * n

        # note that we are not guaranteed that the LNDS ends at n-1
        maxLen = 1
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                
                # verify non-decreasing
                if nums[j] <= nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

                    # we've inherited from the best in range [0...i-1]
                    if dp[i] > maxLen:
                        maxLen = dp[i]
                        break # optimise by early break

        return n - maxLen
    
nums = [2,1,3,2,1]
nums = [1,3,2,1,3,3]
nums = [2,2,2,2,3,3]
nums = [3,3,2]

Solution().minimumOperations(nums)