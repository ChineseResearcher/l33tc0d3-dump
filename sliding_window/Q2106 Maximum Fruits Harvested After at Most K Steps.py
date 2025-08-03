# sliding window - hard
from typing import List
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        n = len(fruits)
        # core ideas:
        # 1) first build a prefix sum of amount over sorted fruits positions
        # 2) use a sliding window to test for different harvest range

        pfSum, rSum = [], 0
        for _, amount in fruits:
            rSum += amount
            pfSum.append(rSum)

        # define a helper to determine the min. cost 
        # for a certain harvest range w/ range denoted by [lb, rb]
        def cost(lb, rb):

            if startPos >= rb:
                return startPos - lb
            
            if startPos <= lb:
                return rb - startPos
            
            # otherwise, we are in range (lb, rb)
            # op1: travel to leftend and go to right end
            op1 = 2 * (startPos - lb) + (rb - startPos)
            op2 = 2 * (rb - startPos) + (startPos - lb)

            return min(op1, op2)

        l, ans = 0, 0
        for r in range(n):

            while l < r and cost(fruits[l][0], fruits[r][0]) > k:
                l += 1

            if cost(fruits[l][0], fruits[r][0]) <= k:
                ans = max(ans, pfSum[r] - (pfSum[l-1] if l > 0 else 0))

        return ans
    
fruits, startPos, k = [[2,8],[6,3],[8,6]], 5, 4
fruits, startPos, k = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4
fruits, startPos, k = [[0,3],[6,4],[8,5]], 3, 2

Solution().maxTotalFruits(fruits, startPos, k)