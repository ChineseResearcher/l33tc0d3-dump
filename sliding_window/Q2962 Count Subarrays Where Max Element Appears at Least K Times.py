# sliding window - medium
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # while we use a sliding window, there's no need for
        # explicit use of left pointer, as we would just record the maxVal indices
        maxValIdx, maxVal = [], max(nums)

        ans = 0
        for r in range(n):
            
            if nums[r] == maxVal:
                maxValIdx.append(r)
                
            # check if we at least have k occurrences of maxVal
            if len(maxValIdx) >= k:
                l = maxValIdx[-k]
                ans += l + 1
                
        return ans
    
nums, k = [1,3,2,3,3], 2
nums, k = [1,4,2,1], 3

Solution().countSubarrays(nums, k)