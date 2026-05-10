# dp - medium
from typing import List
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) dp[i] to denote the max. number of jumps to go to index i
        # 2) O(n^2) loops to explore all (i, j) transition pairs

        dp = [-1] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):

                if dp[j] != -1 and abs(nums[j] - nums[i]) <= target:
                    dp[i] = fmax(dp[i], dp[j] + 1)

        return dp[-1]

nums, target = [0,2,1,3], 1
nums, target = [1,3,6,4,1,2], 2
nums, target = [1,3,6,4,1,2], 3
nums, target = [1,3,6,4,1,2], 0

Solution().maximumJumps(nums, target)