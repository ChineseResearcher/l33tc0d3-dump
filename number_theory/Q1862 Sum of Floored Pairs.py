# number theory - hard
from typing import List
from collections import Counter
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:

        num_freq = Counter(nums)
        # build a freq. arr up to the max. number in nums
        maxNum = max(nums)
        freq = [0] * (maxNum + 1) # dummy-0 in front

        for x in nums:
            freq[x] += 1

        # build a prefix sum over this freq.
        pfSum, cSum = [], 0
        for y in freq:
            cSum += y
            pfSum.append(cSum)

        ans, MOD = 0, int(1e9+7)
        # explore all numbers as the divisor 
        for divisor, f in num_freq.items():

            mul, currAns = 1, 0
            # it is mathematically proved that this loop is a harmonic series
            # which converges to O(logN), making it efficient enough for 1e5 input
            while divisor * mul <= maxNum:

                # suppose divisor = 8
                # and we have possible dividends [8,9,...,15,16,...,23,24,...]
                # for dividends in range [8,15], the floor division over divisor 8 is 1
                # so we sum the freq. of dividends in range [8,15]
                # for dividends in range [16,23], the floor division over 8 is 2
                # and similarly for other ranges

                pfSum_excl = pfSum[divisor * mul - 1]
                if divisor * (mul + 1) - 1 <= maxNum:
                    pfSum_incl = pfSum[divisor * (mul + 1) - 1]
                else:
                    pfSum_incl = pfSum[maxNum]

                currAns += (pfSum_incl - pfSum_excl) * mul 
                currAns %= MOD

                mul += 1

            ans += currAns * f
            ans %= MOD

        return ans
    
nums = [2,5,9]
nums = [7,7,7,7,7,7,7]
# constraint
nums = [1] * int(1e5) + [100000]

Solution().sumOfFlooredPairs(nums)