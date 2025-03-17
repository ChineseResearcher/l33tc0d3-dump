# counting - easy
from collections import Counter
class Solution:
    def divideArray(self, nums):
        for k, v in Counter(nums).items():
            if v % 2 != 0:
                return False

        return True
    
nums = [3,2,3,2,2,2]
nums = [1,2,3,4]

Solution().divideArray(nums)