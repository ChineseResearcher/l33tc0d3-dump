# bit manipulation - medium
from typing import List
from itertools import groupby
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # core idea:
        # 1) bitwise AND only remains the same or reduces
        # 2) due to (1), the max. bitwise AND would be the max. num in nums
        # 3) answer is the longest subarr. containing purely max. num

        max_AND = max(nums)

        ans = 0
        for key, grp in groupby(nums):
            if key == max_AND:
                ans = max(ans, len(list(grp)))

        return ans    
    
nums = [1,2,3,3,2,2]
nums = [1,2,3,4]

Solution().longestSubarray(nums)