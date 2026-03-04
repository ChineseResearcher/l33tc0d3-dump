# dp - hard
from typing import List
from functools import cache
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        m, n = len(nums1), len(nums2)
        fmax = lambda a, b: a if a > b else b
        # since values in each array are unique, proprocess
        # the corresponding indices of unique values
        def get_pos(nums: List[int]) -> dict:

            pos = dict()
            for i, x in enumerate(nums):
                pos[x] = i
            return pos

        pos1, pos2 = get_pos(nums1), get_pos(nums2)

        MOD = int(1e9 + 7)
        @cache
        def f(arr:int, idx:int) -> int:

            # exhausted curr. array
            if arr == 0 and idx == m:
                return 0
            
            if arr == 1 and idx == n:
                return 0
            
            res = 0
            # switching
            if arr == 0 and nums1[idx] in pos2:
                n_idx = pos2[nums1[idx]] + 1
                res = fmax(res, f(1, n_idx) + \
                                (nums2[n_idx] if n_idx < n else 0))
                
            if arr == 1 and nums2[idx] in pos1:
                n_idx = pos1[nums2[idx]] + 1
                res = fmax(res, f(0, n_idx) + \
                                (nums1[n_idx] if n_idx < m else 0))
                
            # continue curr. array
            source = nums1 if arr == 0 else nums2
            length = m if arr == 0 else n
            res = fmax(res, f(arr, idx + 1) + (source[idx+1] if idx+1 < length else 0))

            return res

        return fmax(nums1[0] + f(0, 0), nums2[0] + f(1, 0)) % MOD

nums1, nums2 = [2,4,5,8,10], [4,6,8,9]
nums1, nums2 = [1,3,5,7,9], [3,5,100]
nums1, nums2 = [1,2,3,4,5], [6,7,8,9,10]

Solution().maxSum(nums1, nums2)