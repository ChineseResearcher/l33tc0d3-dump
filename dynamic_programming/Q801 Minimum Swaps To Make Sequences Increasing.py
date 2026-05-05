# dp - hard
from typing import List
from functools import cache
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        # key ideas:
        # 1) solve subproblem (i, prev_swap) where
        # i indicates the subproblem concerning nums1[i:] and nums2[i:]
        # prev_swap indicates if nums1[i-1] and nums2[i-1] were swapped

        @cache
        def f(i: int, prev_swap: bool) -> int:

            if i == n:
                return 0

            a, b = -1, -1
            if i > 0:
                a, b = nums1[i-1], nums2[i-1]

            if prev_swap:
                a, b = b, a

            res = float('inf')
            if nums1[i] > a and nums2[i] > b:
                res = min(res, f(i+1, False))

            if nums2[i] > a and nums1[i] > b:
                res = min(res, 1 + f(i+1, True)) # swapped

            return res

        return f(0, False)

nums1, nums2 = [1,3,5,4], [1,2,3,7]
nums1, nums2 = [0,3,5,8,9], [2,1,4,6,9]

Solution().minSwap(nums1, nums2)