# dp - hard
from typing import List
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        n = len(piles)
        dp = [ [0] * (n+1) for _ in range(k+1) ]

        pf_size, rSum = [], 0
        for i in range(n):
            rSum += len(piles[i])
            pf_size.append(rSum)

        for i in range(1, k+1):
            # considering up to piles[:j]
            for j in range(1, n+1):

                # curr. pile
                cp = piles[j-1]

                # consider the option to take nothing this this pile
                dp[i][j] = max(dp[i][j], dp[i][j-1])

                # prefix sum
                pfSum = 0
                for v in range(len(cp)):
                    # max. picked allowed
                    if v + 1 > i:
                        break

                    pfSum += cp[v]

                    # picking exactly i items would mean that we 
                    # could not have states where the prefix sum of 
                    # sizes up to the j-th pile would be fewer than i
                    acc_cnt = pf_size[j-2] if j-2 >= 0 else 0
                    if acc_cnt >= i-(v+1):
                        dp[i][j] = max(dp[i][j], pfSum + dp[i-(v+1)][j-1])

        return dp[-1][-1] # answer from picking k items

piles, k = [[1,100,3],[7,8,9]], 2
piles, k = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7
piles, k = [[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]], 9

Solution().maxValueOfCoins(piles, k)