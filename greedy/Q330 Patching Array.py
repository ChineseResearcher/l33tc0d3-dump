# greedy - hard
from typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        # the core mathematical underpinning is:
        # for a sorted arr [a, b, c, ...], 
        # if a + 1 >= b, then we can build any sum up to a
        # if a + b + 1 >= c, then we can build any sum up to a + b
        # if a + b + c + 1 >= d, then we can build any sum up to a + b + c
        m = len(nums)

        # keep track of a running sum
        rSum, ans = 0, 0
        for i in range(m):

            while rSum + 1 < nums[i]:
                rSum = 2 * rSum + 1
                ans += 1

                if rSum >= n:
                    return ans
                
            rSum += nums[i]
            if rSum >= n:
                return ans
            
        while rSum < n:
            rSum = 2 * rSum + 1
            ans += 1

        return ans
    
nums, n = [1,3], 6
nums, n = [1,5,10], 20
nums, n = [1,2,2], 5
nums, n = [1,12,15], 43
nums, n = [10,30,36,42,50,76,87,88,91,92], 54

Solution().minPatches(nums, n)