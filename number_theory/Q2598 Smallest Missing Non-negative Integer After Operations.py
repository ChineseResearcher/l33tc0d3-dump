# number theory - medium
from typing import List
from collections import defaultdict
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        n = len(nums)
        # we could definitely achieve numbers in range [0,1,...,n-1]
        # if value is 1 or -1, so the next MEX is just n
        if abs(value) == 1:
            return n

        # how do we quickly determine if the curr. MEX can be formed
        # by some operations on existing numbers?

        # we check if MEX = modulo result of some numbers over value
        # e.g. if we are looking to build MEX = 2, and value = 5, we might
        # have another number 7 where 7 % 5 = 2

        # construct a frequency count of each mod result
        mod_freq = defaultdict(int)
        for x in nums:
            mod_freq[x % value] += 1

        curr_MEX = 0
        while curr_MEX % value in mod_freq:
            mod_freq[curr_MEX % value] -= 1
            if mod_freq[curr_MEX % value] == 0:
                del mod_freq[curr_MEX % value]

            curr_MEX += 1

        return curr_MEX
    
nums, value = [1,-10,7,13,6,8], 5
nums, value = [1,-10,7,13,6,8], 7
nums, value = [3,0,3,2,4,2,1,1,0,4], 5
nums, value = [0,-3], 4

Solution().findSmallestInteger(nums, value)