# dp - hard
from typing import List
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:

        n = len(cuboids)

        cu_ord = []
        for a, b, c in cuboids:
            cu_ord.append(sorted([a, b, c]))

        cu_ord.sort()

        dp, ans = [[0] * 3 for _ in range(n)], 0
        for idx, (a, b, c) in enumerate(cu_ord):
            dp[idx][0] = a
            dp[idx][1] = b
            dp[idx][2] = c

            ans = max(ans, max(dp[idx]))

        # mapping to obtain two remaining dimensions
        od = {0:[1,2], 1:[0,2], 2:[0,1]}
            
        # LIS approach
        for i in range(1, n):

            # O(3)
            for ii in range(3):
                
                d1, d2 = cu_ord[i][od[ii][0]], cu_ord[i][od[ii][1]]
                for j in range(i):
                    
                    # O(3)
                    for jj in range(3):
                        # earlt stop if lower height exceeds (supposed) bounding height
                        if cu_ord[j][jj] > cu_ord[i][ii]:
                            break

                        dd1, dd2 = cu_ord[j][od[jj][0]], cu_ord[j][od[jj][1]]
                        if (dd1 <= d1 and dd2 <= d2) or (dd1 <= d2 and dd2 <= d1):
                            dp[i][ii] = max(dp[i][ii], cu_ord[i][ii] + dp[j][jj])
                            ans = max(ans, dp[i][ii])

        return ans
    
cuboids = [[8,1,5],[1,6,9]]
cuboids = [[38,25,45],[76,35,3]]
cuboids = [[50,45,20],[95,37,53],[45,23,12]]
cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
cuboids = [[74,7,80],[7,52,61],[62,41,37],[91,58,26],[88,98,5],[72,93,23],[56,58,94],[88,8,64],[32,55,5]]

Solution().maxHeight(cuboids)