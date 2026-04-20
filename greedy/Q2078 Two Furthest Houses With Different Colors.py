# greedy - easy
from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n = len(colors)
        fmax = lambda a, b: a if a > b else b

        # key ideas:
        # 1) the greedy thinking tells us that the furthest pair must
        # involve either index 0 and / or index n-1
        # 2) as such we just need to find the first house w/ diff. color
        # against house at left-end and right-end and compare the answer
        if colors[0] != colors[-1]: return n-1

        ans = 0
        for i in range(n-1, 0, -1):
            if colors[i] != colors[0]:
                ans = fmax(ans, i)
                break

        for i in range(n-1):
            if colors[i] != colors[-1]:
                ans = fmax(ans, n-1-i)
                break

        return ans

colors = [0,1]
colors = [1,8,3,8,3]
colors = [1,1,1,6,1,1,1]

Solution().maxDistance(colors)