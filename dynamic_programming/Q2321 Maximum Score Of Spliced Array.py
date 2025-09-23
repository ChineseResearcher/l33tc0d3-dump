# dp - hard
from typing import List
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
        def best_score(baseArr: List[int], swapArr: List[int]) -> int:

            n = len(baseArr)
            # helper to consider building the best score by having
            # the option to swap a subarr. from the swapArr if optimal

            # row 0: unswapped, row 1: swapped
            dp = [ [None] * n for _ in range(2) ]
            dp[0][0], dp[1][0] = baseArr[0], swapArr[0]

            # track a prefix sum from baseArr
            pfSum = baseArr[0]
            for i in range(1, n):
                
                # unswapped inherits from both unswapped and swapped
                dp[0][i] = max(dp[0][i-1], dp[1][i-1]) + baseArr[i]

                # swapped can be:
                # 1) building on prev. swapped
                # 2) start a new swapped subarr.
                dp[1][i] = max(dp[1][i-1], pfSum) + swapArr[i]

                pfSum += baseArr[i]

            return max(dp[0][-1], dp[1][-1])

        res1 = best_score(nums1, nums2)
        res2 = best_score(nums2, nums1)

        return max(res1, res2)
    
nums1, nums2 = [60,60,60], [10,90,10]
nums1, nums2 = [20,40,20,70,30], [50,20,50,40,20]
nums1, nums2 = [7,11,13], [1,1,1]

Solution().maximumsSplicedArray(nums1, nums2)