# sorting - medium
from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # sort nums. arr and greedily form groups (of possibly diff. sizes)
        nums.sort()

        ans, currMin = 1, nums[0]
        for i in range(1, n):

            if nums[i] - currMin > k:
                ans += 1
                currMin = nums[i]

        return ans
    
nums, k = [3,6,1,2,5], 2
nums, k = [1,2,3], 1
nums, k = [2,2,4,5], 0

Solution().partitionArray(nums, k)