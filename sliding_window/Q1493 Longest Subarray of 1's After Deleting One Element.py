# sliding window - medium
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)

        l, window_zero, ans = 0, 0, 0
        for r in range(n):

            if nums[r] == 0:
                window_zero += 1

            while window_zero > 1:
                if nums[l] == 0:
                    window_zero -= 1
                l += 1

            # -1 because we must del one element
            ans = max(ans, r-l+1-1) 

        return ans
    
nums = [0,1,1,1,0,1,1,0,1]
nums = [1,1,0,1]
nums = [1,1,1]
nums = [0,0,0]

Solution().longestSubarray(nums)