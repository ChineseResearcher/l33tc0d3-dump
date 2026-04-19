# two pointers - medium
from typing import List
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        m, n = len(nums1), len(nums2)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) classic two pointers problem with i & j both init. to 0
        # 2) shift i or j based on comparison between nums[i] and nums[j]
        ans = 0

        i, j = 0, 0
        while i < m and j < n:

            if i <= j:
                if nums1[i] <= nums2[j]:
                    ans = fmax(ans, j - i)

            if nums2[j] >= nums1[i]:
                j += 1
            else:
                i += 1

        return ans
    
nums1, nums2 = [2,2,2], [10,10,1]
nums1, nums2 = [30,29,19,5], [25,25,25,25,25]
nums1, nums2 = [55,30,5,4,2], [100,20,10,10,5]

Solution().maxDistance(nums1, nums2)