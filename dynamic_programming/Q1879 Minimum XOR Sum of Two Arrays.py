# dp - hard
from functools import cache
from typing import List
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums2)
        # define terminal cond.
        T = (1 << n) - 1

        fmin = lambda a, b: a if a <= b else b

        @cache
        def f(bitmask: int) -> int:

            # bitmask to record the already picked indices of nums2
            if bitmask == T:
                return 0

            # obtain curr. bit count for indexing nums1
            bc = bitmask.bit_count()
            
            curr_res = float('inf')
            for bit in range(n):
                if (1 << bit) & bitmask == 0:
                    curr_res = fmin(curr_res, (nums1[bit] ^ nums2[bc]) + \
                                    f(bitmask | (1 << bit)))
                    
            return curr_res

        return f(0)
    
nums1, nums2 = [1,2], [2,3]
nums1, nums2 = [1,0,3], [5,3,4]
nums1, nums2 = [100,26,12,62,3,49,55,77,97], [98,0,89,57,34,92,29,75,13]

Solution().minimumXORSum(nums1, nums2)