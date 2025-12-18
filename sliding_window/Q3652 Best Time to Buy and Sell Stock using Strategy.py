# sliding window - medium
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n, k_halved = len(prices), k // 2
        # first build prefix sum on the product of strategy  and prices arr.
        pf_sum, rSum = [], 0
        for i in range(n):
            rSum += prices[i] * strategy[i]
            pf_sum.append(rSum)

        ans = pf_sum[-1]
        fmax = lambda a, b: a if a >= b else b

        # init. windowSum
        windowSum = 0
        for i in range(k_halved, k):
            windowSum += prices[i]

        ans = fmax(ans, windowSum + pf_sum[-1] - pf_sum[k-1])

        for r in range(k, n):
            windowSum += prices[r]
            windowSum -= prices[r - k_halved]

            leftSum = pf_sum[r-k]
            rightSum = pf_sum[-1] - pf_sum[r]

            ans = fmax(ans, leftSum + windowSum + rightSum)

        return ans
    
prices, strategy, k = [4,2,8], [-1,0,1], 2
prices, strategy, k = [5,4,3], [1,1,0], 2

Solution().maxProfit(prices, strategy, k)