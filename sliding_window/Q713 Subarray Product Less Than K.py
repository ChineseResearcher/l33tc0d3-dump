# sliding window - medium
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        l, windowProd, ans = 0, 1, 0
        for r in range(n):
            
            windowProd *= nums[r]
            while l < r and windowProd >= k:
                windowProd //= nums[l]
                l += 1
            
            if windowProd < k:
                ans += (r - l + 1)

        return ans

nums, k = [1,2,3], 0
nums, k = [10,5,2,6], 100

Solution().numSubarrayProductLessThanK(nums, k)