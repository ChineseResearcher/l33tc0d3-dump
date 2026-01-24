# greedy - medium
from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        fmax = lambda a, b: a if a > b else b

        n = len(nums)
        # key ideas:
        # 1) sort the nums array and perform two-pointer traversal
        # 2) the first pointer starts at the head, while the second starts at the tail
        # 3) greedily track the max. pair sum that arises as we form pairs
        # (nums[0], nums[-1]) -> (nums[1], nums[-2]) -> ... -> (nums[n//2-1], nums[n//2])
        nums.sort()

        l, r = 0, n-1
        ans = 0
        while l < r:

            ans = fmax(ans, nums[l] + nums[r])
            l += 1
            r -= 1

        return ans

nums = [1,3,8,9]
nums = [3,5,4,2,4,6]

Solution().minPairSum(nums)