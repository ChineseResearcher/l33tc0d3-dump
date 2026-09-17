# dp - medium
from typing import List
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) sliding window + DP
        # 2) build a linear 2 x N DP table with 2 states: picked1, picked2

        dp = [ [float('inf')] * n for _ in range(2) ]

        l, windowSum = 0, 0 
        for r in range(n):

            windowSum += arr[r]
            while l < r and windowSum > target:
                windowSum -= arr[l]
                l += 1

            # skip options:
            if r > 0:
                dp[0][r] = dp[0][r - 1]
                dp[1][r] = dp[1][r - 1]

            # found a valid subarr [l...r] 
            if windowSum == target:
                subarrLen = r - l + 1
                # treat curr. subarr. as the 1st found subarr.
                dp[0][r] = fmin(dp[0][r], subarrLen)
                # treat curr. subarr. as the 2nd found subarr.
                dp[1][r] = fmin(
                    dp[1][r], 
                    (dp[0][l - 1] if l > 0 else float('inf')) + subarrLen
                                )

        return dp[1][n - 1] if dp[1][n - 1] < float('inf') else -1

arr, target = [7,3,4,7], 7
arr, target = [3,2,2,4,3], 3
arr, target = [4,3,2,6,2,3,4], 6
arr, target = [1,1,1,2,2,2,4,4], 6

Solution().minSumOfLengths(arr, target)