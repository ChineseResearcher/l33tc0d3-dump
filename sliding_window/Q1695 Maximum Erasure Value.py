# sliding window - medium
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        # maintain a sliding window which contains unique element
        window = set()

        ans, l = 0, 0

        curr_w_sum = 0
        for r in range(n):

            while nums[r] in window:
                window.discard(nums[l])
                curr_w_sum -= nums[l]
                l += 1
            
            curr_w_sum += nums[r]
            window.add(nums[r])
            ans = max(ans, curr_w_sum)

        return ans
    
nums = [4,2,4,5,6]
nums = [5,2,1,2,5,2,1,2,5]

Solution().maximumUniqueSubarray(nums)