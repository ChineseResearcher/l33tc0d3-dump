# greedy - medium
from typing import List
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # sort the nums to ensure greedy method works
        nums.sort()

        # make first number nums[0] - k
        nums[0] -= k

        ans = 1
        for i in range(1, n):

            # allowed range: [nums[i] - k, nums[i] + k]
            lb, ub = nums[i] - k, nums[i] + k
            if lb > nums[i-1]:
                nums[i] = lb

            # our goal is to make the updated nums arr.
            # monotonically increasing to the best extent 
            # while greedily applying adjustment up to k
            else:
                nums[i] = min(nums[i-1] + 1, ub)

            if nums[i] > nums[i-1]:
                ans += 1

        return ans
    
nums, k = [1,2,2,3,3,4], 2
nums, k = [4,4,4,4], 1

Solution().maxDistinctElements(nums, k)