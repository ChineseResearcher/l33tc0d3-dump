# dp - hard
from typing import List
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return 0

        # generate a 2-D dp where a counter dict is nested in dp[i]
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):

                diff = nums[i] - nums[j]
                # increment the number of subseq. ending at nums[i] w/ this diff
                dp[i][diff] += 1 + dp[j][diff]

        # then we collect the answer by visiting each dp[i] and its diff
        # note: we need to subtract each count by some prefix freq.
        # to disregard arithmetic seq. of length-2
        prefix_freq = defaultdict(int)

        # init. the first two elements
        prefix_freq[nums[0]] += 1
        prefix_freq[nums[1]] += 1

        ans = 0
        for i in range(2, n):
            for diff, f in dp[i].items():
                ans += f - prefix_freq[nums[i] - diff]
            # mark this number
            prefix_freq[nums[i]] += 1

        return ans
    
nums = [2,4,6,8,10]
nums = [7,7,7,7,7]

Solution().numberOfArithmeticSlices(nums)