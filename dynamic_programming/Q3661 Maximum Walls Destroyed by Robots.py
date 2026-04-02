# dp - hard
import bisect
from typing import List
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        
        n = len(robots)
        # key ideas:
        # 1) sort the distance array based on positions of robots,
        # and also sort walls array for binary search later

        # 2) dp table is init. to 2 x n, where dp[0][i] represents
        # the max. cnt of robots destroyed if we consider up to the i-th robot
        # and that the i-th robot is shooting to the left (dp[1][...] shoots right)

        # 3) also maintain an auxiliary maintaining the rightmost bound
        # if the i-th robot is to shoot to the right
        t = [(x, i) for i, x in enumerate(robots)]
        t.sort()

        d = [distance[i] for _, i in t]
        walls.sort()
        w = set(walls)

        # helper to determine effective left bound
        def get_lb1(idx:int, pos:int) -> int:
            lb = float('-inf')
            if idx > 0:
                lb = max(lb, rb_arr[idx-1] + 1) # prev bot's right bound
            lb = max(lb, pos - d[idx])
            return lb

        def get_lb2(idx:int, pos:int) -> int:
            lb = float('-inf')
            if idx > 0:
                lb = max(lb, t[idx-1][0] + 1) # prev bot's position
            lb = max(lb, pos - d[idx])
            return lb

        # helper to determine effective right bound
        def get_rb(idx:int, pos:int) -> int:
            rb = float('inf')
            if idx + 1 < n:
                rb = min(rb, t[idx+1][0])
            rb = min(rb, pos + d[idx])
            return rb

        rb_arr = [0] * n
        dp = [ [0] * n for _ in range(2) ]
        for i in range(n):

            # get curr. robot's position
            pos = t[i][0]

            # shoot left + prev. shoot right
            shoot_left1 = 0
            lb = get_lb1(i, pos)
            if lb <= pos:
                shoot_left1 = bisect.bisect_right(walls, pos) - bisect.bisect_left(walls, lb)

            # shoot left + prev. shoot left
            shoot_left2 = 0
            lb = get_lb2(i, pos)
            if lb <= pos:
                shoot_left2 = bisect.bisect_right(walls, pos) - bisect.bisect_left(walls, lb)

            dp[0][i] = max(dp[0][i], shoot_left1 + (dp[1][i-1] if i > 0 else 0))
            dp[0][i] = max(dp[0][i], shoot_left2 + (dp[0][i-1] if i > 0 else 0))

            # shoot right + prev. shoot left
            shoot_right1 = 0
            rb = get_rb(i, pos)
            if rb >= pos:
                shoot_right1 = bisect.bisect_right(walls, rb) - bisect.bisect_left(walls, pos)

            # shoot right + prev. shoot right
            shoot_right2 = shoot_right1
            if i > 0 and rb_arr[i-1] == pos and pos in w:
                shoot_right2 -= 1
            
            dp[1][i] = max(dp[1][i], shoot_right1 + (dp[0][i-1] if i > 0 else 0))
            dp[1][i] = max(dp[1][i], shoot_right2 + (dp[1][i-1] if i > 0 else 0))
            rb_arr[i] = rb # update right bound

        return max(dp[0][-1], dp[1][-1])

robots, distance, walls = [4], [3], [1,10]
robots, distance, walls = [10,2], [5,1], [5,2,7]
robots, distance, walls = [1,2], [100,1], [10]

Solution().maxWalls(robots, distance, walls)