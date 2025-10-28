# prefix sum - easy
from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        n = len(nums)
        # no need to simulate as we can rely on
        # prefix and suffix sums directly to determine whether an index is valid
        pfSum, cSum = [], 0
        for x in nums:
            cSum += x
            pfSum.append(cSum)

        ans = 0
        for i in range(n):
            # potential starting point
            if nums[i] == 0:

                ls = pfSum[i-1] if i-1 >= 0 else 0
                rs = pfSum[-1] - pfSum[i]

                if ls == rs:
                    ans += 2 # valid for both left/right

                if abs(ls - rs) == 1:
                    ans += 1 # valid for either left/right

        return ans
    
nums = [1,0,2,0,3]
nums = [2,3,4,0,4,1,0]
nums = [16,13,10,0,0,0,10,6,7,8,7]

Solution().countValidSelections(nums)