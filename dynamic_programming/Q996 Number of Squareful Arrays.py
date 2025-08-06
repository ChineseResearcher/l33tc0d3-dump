# dp - hard
from typing import List
from functools import cache
from collections import Counter
import math
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:

        n = len(nums)
        # core ideas:
        # 1) use memoized dfs to solve the problem, keep track of 
        # the usage bitmask and prev. chosen number
        # 2) simply sum all subproblems to obtain the answer
        # 3) discount duplicates by pre-computing the occurrences of numbers

        # to indicate full usage bitmask
        full = (1 << n) - 1

        # for (3)
        freq = Counter(nums)
        discount = 1
        for v in freq.values():
            discount *= math.factorial(v)

        @cache
        def recursive_build(mask, seq):
            
            if mask == full:
                return 1
            
            if seq:
                prev = int(seq[:-1].split('_')[-1])
            else:
                prev = -1

            curr_res = 0
            for i in range(n):
                # encounter missing num
                if mask & (1 << i) == 0:
                    
                    # form the curr. pair sum
                    cps = nums[i] + prev
                    if prev == -1 or int((cps ** 0.5)) ** 2 == cps:
                        mask |= (1 << i)
                        curr_res += recursive_build(mask, seq + str(nums[i]) + '_')
                        mask &= ~(1 << i) # roll-back mask update

            return curr_res

        return recursive_build(0, '') // discount
    
nums = [1,17,8]
nums = [2,2,2]
nums = [65,44,5,11]
nums = [2] * 12

Solution().numSquarefulPerms(nums)