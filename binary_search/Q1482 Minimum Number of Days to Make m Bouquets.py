# binary search - medium
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)
        fmin = lambda a, b: a if a < b else b
        # impossible to produce "m" bouquets when the count of
        # k-length consecutive slots does not equal or exceed "m"
        if n // k < m: return -1

        # key ideas:
        # 1) binary search on the answer (min. days required)
        # 2) linear pass to check if it's feasible for target no. of days

        def isFeasible(target:int) -> bool:
            rSum, bouquet_cnt = 0, 0
            for i in range(n):
                if target >= bloomDay[i]:
                    rSum += 1
                else:
                    rSum = 0 # reset

                if rSum == k:
                    bouquet_cnt += 1
                    rSum = 0 # reset

            return bouquet_cnt >= m

        l, r = 0, max(bloomDay)
        ans = r
        while l <= r:

            mid = (l + r) // 2
            if isFeasible(mid):
                ans = fmin(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans

bloomDay, m, k = [1,10,3,10,2], 3, 1
bloomDay, m, k = [1,10,3,10,2], 3, 2
bloomDay, m, k = [7,7,7,7,12,7,7], 2, 3

Solution().minDays(bloomDay, m, k)