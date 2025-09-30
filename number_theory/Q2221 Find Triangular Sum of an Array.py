# number theory - medium
from typing import List
import math
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        n = len(nums)

        ans = 0
        for i, num in enumerate(nums):
            # use of Pascal's triangle as coefficients
            ans += (math.comb(n-1, i) * num) % 10
            ans %= 10

        return ans

nums = [1,2,3,4,5]
nums = [1] * int(1e3)

Solution().triangularSum(nums)