# greedy - medium
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxVol = 0

        while l < r:
            
            holding_height = min(height[l], height[r])
            vol = holding_height * (r - l)
            maxVol = max(maxVol, vol)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxVol

height = [1,1]
height = [1,8,6,2,5,4,8,3,7]

Solution().maxArea(height)
