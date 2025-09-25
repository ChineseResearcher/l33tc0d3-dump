# dp - medium
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        # row-wise dp that grows in size to max. length n
        dp = [triangle[0][0]]

        for r in range(1, n):

            new_dp = [float('inf')] * (r+1)
            for c in range(r+1):

                if 0 <= c <= r-1:
                    new_dp[c] = min(new_dp[c], dp[c] + triangle[r][c])

                if 0 <= c-1 <= r-1:
                    new_dp[c] = min(new_dp[c], dp[c-1] + triangle[r][c])

            # override dp
            dp = new_dp

        return min(dp)
    
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# constraint
import random
triangle = [ [random.randint(-10000,10000) for _ in range(i)] for i in range(1, 201)]

Solution().minimumTotal(triangle)