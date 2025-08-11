# number theory - hard
from typing import List
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:

        n = len(nums)
        # core ideas:
        # 1) first sort the numbers as we do not care about the order of elements
        # in any subsequence, just the min / max

        # 2) for a length-k subseq. [i, i+1, i+2, ..., j], we know the "width" of this subseq.
        # is just j - i, and there can be 2 ** (k-2) such subsequences w/ the same width 

        # 3) through observations we can exhaust all possible length-k subseq. for k in range [0, n-2]
        # and compute the associated sum of power-2 in O(1) time
        nums.sort()

        # build a prefix sum
        pfSum, currSum = [], 0
        for x in nums:
            currSum += x
            pfSum.append(currSum)

        ans, MOD = 0, int(1e9 + 7)
        for k in range(n-1):

            p1 = pfSum[-1] - pfSum[k]
            p2 = pfSum[(n-1) - (k+1)]
            ans += pow(2, k, MOD) * (p1 - p2)
            ans %= MOD

        return ans
    
nums = [2]
nums = [2,1,3]
nums = [1,2,3,5,6]

Solution().sumSubseqWidths(nums)