# two pointers - medium
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        n = len(nums)
        # valid triangle is defined as:
        # sum of any two side length greater than the remaining side length

        # if we sort our nums, we just have to make sure that the smaller two num always
        # exceed the largest num placed rightmost (i.e. fixing the largest)
        nums.sort()

        result = 0
        for i in range(n-1, 1, -1):

            left, right = 0, i-1
            # fix the largest
            fixed = nums[i]

            while left < right:
                if nums[left] + nums[right] > fixed:
                    # this implies any number >= nums[left] would form a valid triangle too
                    # with the same nums[right], so increment by right - left
                    result += right - left
                    right -= 1
                else:
                    left += 1
                    
        return result
    
nums = [2,2,3,4]
nums = [4,2,3,4]
nums = [7,0,0,0]

Solution().triangleNumber(nums)