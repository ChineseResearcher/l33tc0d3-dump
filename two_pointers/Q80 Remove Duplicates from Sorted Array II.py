# two pointer - medium
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        # second pointer for final result placement
        j = 0

        # maintain reference to curr number and freq
        curr_num, curr_freq = float('-inf'), 0

        for i in range(n):

            # update number and freq
            if nums[i] > curr_num:
                curr_num, curr_freq = nums[i], 1
            else:
                curr_freq += 1

            # override with j pointer
            if curr_freq <= 2:
                nums[j] = curr_num
                j += 1

        return j

nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]

Solution().removeDuplicates(nums)