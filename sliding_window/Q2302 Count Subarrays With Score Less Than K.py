# sliding window - hard
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # window keeps growing as long as windowSum * (r-l+1) < k
        windowSum = 0

        l, ans = 0, 0
        for r in range(n):
            
            # if nums[r] is already >= k, immediately 
            # invalidate the curr. window
            if nums[r] >= k:
                l = r + 1
                windowSum = 0
                continue
            
            windowSum += nums[r]
            while windowSum * (r-l+1) >= k:
                windowSum -= nums[l]
                l += 1
                
            # after above, the score of nums[l:r+1] is 
            # cetainly below k, we can increment ans accordingly
            ans += r - l + 1
            
        return ans
    
nums, k = [2,1,4,3,5], 10
nums, k = [1,1,1], 5

Solution().countSubarrays(nums, k)