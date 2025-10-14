# dp - hard
from typing import List
from collections import defaultdict
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:

        n = len(nums)
        # 1-D DP arr. where dp[i] stores the sum of all good subseq. ending at nums[i]
        # note: each element in nums is already a good subsequence (of length-1)
        dp = [x for x in nums]

        # maintain two dict storing the dp val. sum and freq. sum for each unique number
        val_sum = defaultdict(int)
        freq_sum = defaultdict(int)

        MOD = int(1e9 + 7)
        for i in range(n):

            curr = nums[i]
            freq_sum[curr] += 1
            # check for valid precedent:
            # i.e. either nums[i] + 1 or nums[i] - 1 exists
            if curr + 1 in val_sum:

                dp[i] += val_sum[curr + 1]
                dp[i] += freq_sum[curr + 1] * curr
                freq_sum[curr] += freq_sum[curr + 1]

            if curr - 1 in val_sum:

                dp[i] += val_sum[curr - 1]
                dp[i] += freq_sum[curr - 1] * curr
                freq_sum[curr] += freq_sum[curr - 1]

            dp[i] %= MOD
            val_sum[curr] += dp[i]
            val_sum[curr] %= MOD  

        return sum(val_sum.values()) % MOD
    
nums = [1,2,1]
nums = [3,4,5]
# constraint
import random
nums = [random.randint(1, int(1e5)) for _ in range(int(1e5))]

Solution().sumOfGoodSubsequences(nums)