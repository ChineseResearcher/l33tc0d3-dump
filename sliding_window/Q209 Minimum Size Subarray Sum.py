# sliding window - medium
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) move a sliding window, and shrink whenever windowSum is at least target
        # 2) track the min. size of all such shrunk windows

        l, windowSum, ans = 0, 0, n + 1
        for r in range(n):
            windowSum += nums[r]
            while windowSum >= target:
                ans = fmin(ans, r - l + 1)
                windowSum -= nums[l]
                l += 1

        return ans if ans <= n else 0
    
target, nums = 4, [1,4,4]
target, nums = 6, [10,2,3]
target, nums = 7, [2,3,1,2,4,3]
target, nums = 11, [1,1,1,1,1,1,1,1]

Solution().minSubArrayLen(target, nums)