# array - medium
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0

        for c in nums:

            if c == 0:
                red += 1

            elif c == 1:
                white += 1

            else:
                blue += 1

        # fill red, white, blue in order
        for i in range(len(nums)):

            if red > 0:
                nums[i] = 0
                red -= 1
                continue

            if white > 0:
                nums[i] = 1
                white -= 1
                continue

            if blue > 0:
                nums[i] = 2
                blue -= 1

nums = [0,2]
nums = [2,0,1]
nums = [2,0,2,1,1,0]