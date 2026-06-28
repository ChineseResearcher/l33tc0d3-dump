# binary search - medium
from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        n = len(position)
        # key ideas:
        # 1) classic MaxiMin problem, approach by Binary Search on the answer
        # 2) for the target answer, run an O(n) check to test if m balls
        # can be placed into n baskets with a pairwise distance >= target
        position.sort()

        def canPlace(minDist:int) -> bool:
            # init. by placing first ball in the first basket
            cnt, prev = 1, position[0]
            for i in range(1, n):
                if position[i] - prev >= minDist:
                    cnt += 1
                    if cnt == m:
                        return True
                    prev = position[i]
            return False

        l, r = 1, (position[-1] - position[0]) // (m-1)
        ans = 0
        while l <= r:

            mid = (l + r) // 2
            if canPlace(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1

        return ans

position, m = [1,2,3,4,7], 3
position, m = [5,4,3,2,1,1000000000], 2

Solution().maxDistance(position, m)