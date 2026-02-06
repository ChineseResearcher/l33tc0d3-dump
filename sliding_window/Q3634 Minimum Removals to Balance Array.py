# sliding window - medium
from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) after sorting, use a sliding window to maintain a valid
        # range where nums[l] <= k * nums[r], and the no. of removals is n-(r-l+1)
        # 2) init. our ans to n-1 as it would at most take n-1 removals
        # to make min(nums) <= k * max(nums)
        nums.sort()

        l, ans = 0, n-1
        for r in range(n):
            while nums[r] > k * nums[l]:
                l += 1
            ans = fmin(ans, n-(r-l+1))

        return ans
    
nums, k = [4,6], 2
nums, k = [2,1,5], 2
nums, k = [1,6,2,9], 3

Solution().minRemoval(nums, k)