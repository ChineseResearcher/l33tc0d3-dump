# sliding window - medium
from typing import List
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        # use a sliding window that expands 
        # as long as the subarr is strictly increasing
        l = 0

        # track the length of prev. window length
        # note: it is at least 1
        prev_w = 1

        ans = 0
        for r in range(1, n):

            # in the case of window breaking (i.e. nums[i] <= nums[i-1])
            # we move the left pointer to represent a new window
            if nums[r] <= nums[r-1]:
                # override previous window width
                prev_w = r-l
                l = r

            # update our answer via two scenarios
            # 1) the smaller of previous and current window
            # 2) current window in half
            op1 = min(prev_w, r-l+1)
            if op1 > ans:
                ans = op1

            op2 = (r-l+1) // 2
            if op2 > ans:
                ans = op2

        return ans

nums = [2,5,7,8,9,2,3,4,3,1]
nums = [1,2,3,4,4,4,4,5,6,7]
nums = [-6,-2,-8,7,-12]

Solution().maxIncreasingSubarrays(nums)