# dp - medium
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        # two 1-D dps to store the maximum subarr sum ending at index i
        dp_max, dp_min = [0]*n, [0]*n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        ans = nums[0]
        for i in range(1, n):
            
            # it is possible for prev. dp to be 0, in this case
            # it is more optimal include the curr. num as the start of the seq.
            dp_max[i] = max(max(nums[i] * dp_max[i-1], nums[i] * dp_min[i-1]), nums[i])
            dp_min[i] = min(min(nums[i] * dp_max[i-1], nums[i] * dp_min[i-1]), nums[i])

            ans = max(ans, dp_max[i])

        return ans
    
nums = [2,3,-2,4]
nums = [-2,0,-1]
nums = [0,2]
nums = [-2,3,-4]

Solution().maxProduct(nums)