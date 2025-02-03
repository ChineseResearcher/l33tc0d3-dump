# array - easy
class Solution:
    def longestMonotonicSubarray(self, nums) -> int:
        n = len(nums)
        ans = 1 # min. length of subarr.

        # one pass for strictly increasing
        l = 0
        for r in range(1, n):
            if nums[r] <= nums[r-1]:
                ans = max(ans, r-l)
                l = r
                continue

            if r == n-1: ans = max(ans, r-l+1)

        # one pass for strictly decreasing
        l = 0
        for r in range(1, n):
            if nums[r] >= nums[r-1]:
                ans = max(ans, r-l)
                l = r
                continue

            if r == n-1: ans = max(ans, r-l+1)

        return ans
    
nums = [1,4,3,3,2]
nums = [1,2,3,1,1,2,3,4]
nums = [3,2,1,2]

Solution().longestMonotonicSubarray(nums)