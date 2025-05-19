# two pointers - medium
from typing import List
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # split the nums. arr into two halves and facilitate
        # comparisons between the curr. element in first & second halve
        k = n // 2

        first_halve, second_halve = nums[:k], nums[k:]
        # init. two pointers to track the curr. positions in two arrs.
        i, j = 0, 0

        delPairs = 0
        while i < len(first_halve):
            
            while j < len(second_halve) and second_halve[j] <= first_halve[i]:
                j += 1
                
            if j == len(second_halve):
                break
                
            if first_halve[i] < second_halve[j]:
                delPairs += 1
                i += 1
                j += 1
                
        return n - delPairs * 2
    
nums = [1,2,3,4]
nums = [1,1,2,2,3,3]
nums = [1000000000,1000000000]
nums = [2,3,4,4,4]
nums = [2,3,4]
nums = [1,1,2,5,6]
nums = [3,4,7,8,9,9]
nums = [1,1,2,2,2,3,3,3,3]

Solution().minLengthAfterRemovals(nums)