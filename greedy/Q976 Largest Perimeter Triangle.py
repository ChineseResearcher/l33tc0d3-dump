# greedy - easy
from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        n = len(nums)
        # sort then apply greedying thinking
        nums.sort()

        # suppose we select three side lengths a, b, c from sorted nums
        # where a <= b <= c, it is guaranteed that for every c, the
        # best valid (a, b) that would yield the largest perimeter
        # is going to be consecutive such that (a, b, c) are at indices 
        # (i, i+1, i+2)

        for i in range(n-1, 1, -1):
            a, b, c = nums[i-2], nums[i-1], nums[i]
            # only need to check if a + b > c
            if a + b <= c:
                continue

            return a + b + c

        return 0
    
nums = [2,1,2]
nums = [1,2,1,10]

Solution().largestPerimeter(nums)