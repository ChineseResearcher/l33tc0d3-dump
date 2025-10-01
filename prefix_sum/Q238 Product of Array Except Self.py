# prefix sum - medium
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        # answer arr. excluded from space complexity, so we have O(1) SC
        ans = [1] * n
        # build forward cumulative prod.
        cProd = 1
        for i in range(n):
            if i-1 >= 0:
                cProd *= nums[i-1]
            ans[i] *= cProd

        # build backward cumulative prod.
        cProd = 1
        for j in range(n-1, -1, -1):
            if j+1 < n:
                cProd *= nums[j+1]
            ans[j] *= cProd

        return ans
    
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]

Solution().productExceptSelf(nums)