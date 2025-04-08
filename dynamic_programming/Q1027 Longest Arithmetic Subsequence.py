# dp - medium
from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, nums) -> int:
        n = len(nums)
        # construct dp arr. of size n storing the longest
        # subseq. if nums[i] is involved
        dp = [0] * n

        # we also need an auxiliary dict to store the 
        # length of different arithmetic seq. at idx i
        arithSeq = {idx: defaultdict(int) for idx in range(n)}

        ans = 0
        for i in range(1, n):
            for j in range(i-1, -1, -1):

                # similar to the classic LIS problem, we search
                # for prev. state to inherit from if an active arithmetic
                # subseq. of diff = nums[i] - nums[j] is present
                diff = nums[i] - nums[j]
                if arithSeq[i][diff] == 0:

                    # to start an active seq., increment length by 2
                    if arithSeq[j][diff] == 0:
                        arithSeq[i][diff] += 2
                    else:
                        arithSeq[i][diff] = arithSeq[j][diff] + 1

                    # dp[i] would track the max.
                    dp[i] = max(dp[i], arithSeq[i][diff])

            ans = max(ans, dp[i])

        return ans
    
nums = [20,1,15,3,10,5,8]
nums = [9,4,7,2,10]
nums = [3,6,9,12]
nums = [1,2]

Solution().longestArithSeqLength(nums)