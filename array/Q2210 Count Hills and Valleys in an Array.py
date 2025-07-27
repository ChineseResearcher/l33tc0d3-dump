# array - easy
from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        n = len(nums)
        # as per hint of @user6403HI:
        # count direction change instead of hill / valley

        # keep track of the first index where there's a direction
        j, curr_dir = 1, -1
        while j < n:

            if nums[j] > nums[j-1]:
                curr_dir = 1
                break

            if nums[j] < nums[j-1]:
                curr_dir = 0
                break

            j += 1

        ans = 0
        for i in range(j+1, n):

            if curr_dir == 1 and nums[i] < nums[i-1]:
                # hill
                ans += 1
                curr_dir = 0

            if curr_dir == 0 and nums[i] > nums[i-1]:
                # valley
                ans += 1
                curr_dir = 1

        return ans
    
nums = [2,4,1,1,6,5]
nums = [6,6,5,5,4,1]

Solution().countHillValley(nums)