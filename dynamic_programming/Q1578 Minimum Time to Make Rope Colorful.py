# dp - medium
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        n = len(colors)
        # consider DP where dp[i] is the min. amt of time needed
        # to make the sequence colorful for up to the i-th balloon
        dp = [0] * n

        # init. a variable that track the max. time
        # for a section of repeating colors
        rMax = 0

        for i in range(1, n):

            dp[i] = dp[i-1]
            if colors[i] != colors[i-1]:
                rMax = 0
                continue

            # otherwise, we have a repeating color
            if rMax == 0:
                dp[i] += neededTime[i-1]
            dp[i] += neededTime[i]
            dp[i] += rMax # rMax as of dp[i-1]

            rMax = max(rMax, max(neededTime[i-1], neededTime[i]))
            dp[i] -= rMax

        return dp[-1]

colors, neededTime = "abaac", [1,2,3,4,5]
colors, neededTime = "aaaaa", [1,2,3,4,3]
colors, neededTime = "abc", [1,2,3]
colors, neededTime = "aabaa", [1,2,3,4,1]

Solution().minCost(colors, neededTime)