# simulation - medium
from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) notice that every time we rotate the function, the 
        # number at the supposed right end of the arr. gets reduced to 0
        # and at the same time, every other number gets incremented by a multiplier of 1
        # 2) we can simulate the process and obtain the max. F(k)

        currSum = sum([i * nums[i] for i in range(n)])
        arrSum = sum(nums)

        ans = currSum
        while nums:
            
            x = nums.pop()
            currSum -= x * (n-1)
            currSum += (arrSum - x)

            ans = fmax(ans, currSum)

        return ans

nums = [100]
nums = [4,3,2,6]

Solution().maxRotateFunction(nums)