# greedy - medium
from typing import List
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))
    
nums, k = [1,3,2], 2
nums, k = [4,2,5,1], 3

Solution().maxTotalValue(nums, k)