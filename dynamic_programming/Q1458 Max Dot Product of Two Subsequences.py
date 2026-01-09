# dp - hard
from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        m, n = len(nums1), len(nums2)

        # knapsack dp initiation
        dp = [ [float('-inf')] * n for _ in range(m) ]
        dp[0][0] = nums1[0] * nums2[0]

        fmax = lambda a, b: a if a > b else b

        # limit to only nums2[0], explore nums1[1...m]
        for i in range(1, m):
            dp[i][0] = fmax(dp[i-1][0], nums1[i] * nums2[0])

        # limit to only nums1[0], explore nums2[1...n]
        for i in range(1, n):
            dp[0][i] = fmax(dp[0][i-1], nums2[i] * nums1[0])

        for i in range(1, m):
            for j in range(1, n):

                # take option
                if dp[i-1][j-1] >= 0:
                    dp[i][j] = fmax(dp[i][j], dp[i-1][j-1] + fmax(nums1[i] * nums2[j], 0))
                else:
                    dp[i][j] = fmax(dp[i][j], nums1[i] * nums2[j])

                # skip options
                dp[i][j] = fmax(dp[i][j], dp[i-1][j])
                dp[i][j] = fmax(dp[i][j], dp[i][j-1])

        return dp[-1][-1]
    
nums1, nums2 = [2,1,-2,5], [3,0,-6]
nums1, nums2 = [3,-2], [2,-6,7]
nums1, nums2 = [-1,-1], [1,1]
nums1, nums2 = [-3,-8,3,-10,1,3,9], [9,2,3,7,-9,1,-8,5,-1,-1]

Solution().maxDotProduct(nums1, nums2)