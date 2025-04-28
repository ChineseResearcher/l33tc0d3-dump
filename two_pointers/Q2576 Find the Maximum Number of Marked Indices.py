# two pointers - medium
from typing import List
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        # idea is similar to LC2856 except that we have to
        # sort in ascending first for this problem
        nums.sort()

        k = n // 2
        # apply two pointers to to separate arrays
        first_halve, second_halve = nums[:k], nums[k:]
        # init. two pointers to track the curr. positions in two arrs.
        i, j = 0, 0

        marked = 0
        while i < len(first_halve):
            
            # the pairing condition is s.t. nums[j] >= nums[i] * 2
            while j < len(second_halve) and second_halve[j] < 2 * first_halve[i]:
                j += 1
                
            if j == len(second_halve):
                break
                
            if 2 * first_halve[i] <= second_halve[j]:
                # mark the curr. pair
                marked += 2
                i += 1
                j += 1
                
        return marked
    
nums = [3,5,2,4]
nums = [9,2,5,4]
nums = [7,6,8]

Solution().maxNumOfMarkedIndices(nums)