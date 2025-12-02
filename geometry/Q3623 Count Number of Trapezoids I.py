# geometry - medium
from collections import defaultdict
from typing import List
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        # key ideas:
        # 1) a valid horizontal trapezoid need to have top / bottom parallel to x-axis
        # 2) we can view this as a combinatorics problem where for a certain y,
        # with k >= 2 points, we have kC2 ways to form the top or bottom
        # 3) use a hashmap to build the count of points at each y-axis point
        # and apply combinatorics thereafter to obtain the answer
        y_cnt = defaultdict(int)

        for _, y in points:
            y_cnt[y] += 1

        # collect kC2 results
        kC2 = []
        for _, k in y_cnt.items():
            if k >= 2:
                kC2.append(k * (k-1) // 2) # kC2


        # suppose there are m items in kC2, there are 
        # m + (m-1) + (m-2) + ... + 1 ways to form unique horizontal trapezoids
        ans, combTotal = 0, sum(kC2)

        MOD = int(1e9 + 7)
        for c in kC2:
            combTotal -= c
            ans += c * combTotal
            ans %= MOD

        return ans

points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
points = [[0,0],[1,0],[0,1],[2,1]]

Solution().countTrapezoids(points)