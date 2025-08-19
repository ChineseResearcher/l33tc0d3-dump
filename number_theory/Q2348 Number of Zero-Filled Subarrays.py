# number theory - medium
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        ans, zero_cnt = 0, 0
        for x in nums:

            if x == 0:
                zero_cnt += 1
                ans += zero_cnt
                
            else:
                zero_cnt = 0
        
        return ans
    
nums = [1,3,0,0,2,0,0,4]
nums = [0,0,0,2,0,0]
nums = [2,10,2019]

Solution().zeroFilledSubarray(nums)