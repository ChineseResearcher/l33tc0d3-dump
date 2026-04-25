# geometry - hard
from typing import List, Tuple
from collections import deque
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:

        # key ideas:
        # 1) how do we determine if a new point to be added to be k-selection
        # can achieve a minimum pairwise manhattan dist. no smaller than "target"?
        # 2) we could efficiently answer the above by sorting the on-the-boundary
        # points in clockwise manner, starting from (0,0) facing north

        v_pt = {0:[], side:[]}
        h_pt = {0:[], side:[]}
        for x, y in points:
            # vertical points
            if x == 0:
                v_pt[0].append((x,y))
            if x == side:
                v_pt[side].append((x,y))

            # horizontal points
            if y == 0:
                h_pt[0].append((x,y))
            if y == side:
                h_pt[side].append((x,y))

        clockwise = sorted(v_pt[0]) + sorted(h_pt[side]) + \
                    sorted(v_pt[side], reverse=True) + sorted(h_pt[0], reverse=True)

        n = len(clockwise)

        # helper for manhattan dist.
        def mht_dist(c1: Tuple[int, int], c2: Tuple[int, int]) -> int:
            return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

        # helper to check if target min. pairwise dist. is valid
        def isValid(target:int) -> bool:

            # one issue is that the first point in clockwise
            # might not be the optimal first point to include 
            
            # we would use a heuristic process by trying out all points in clockwise
            # as the potential starting point to be selected

            # this would involve a nested binary search that maximally jumps k times
            # and that the search array is shuffled at most n times
            arr = deque(clockwise[:])
            shuffle = 0

            while shuffle < n:
                
                chosen = [0]
                # use binary search to find the next index with threshold dist.
                while len(chosen) < k:

                    l, r, nidx = chosen[-1]+1, n-1, n
                    while l <= r:

                        mid = (l + r) // 2
                        if mht_dist(arr[mid], arr[chosen[-1]]) >= target:
                            nidx = min(nidx, mid)
                            r = mid - 1
                        else:
                            l = mid + 1

                    if nidx < n:
                        chosen.append(nidx)
                    else:
                        break

                if len(chosen) == k:
                    if mht_dist(arr[chosen[0]], arr[chosen[-1]]) >= target:
                        return True
                
                # otherwise, shuffle
                arr.append(arr.popleft())
                shuffle += 1

            return False

        l, r, ans = 1, 2 * side, 0
        while l <= r:

            target = (l + r) // 2
            if isValid(target):
                ans = max(ans, target)
                l = target + 1
            else:
                r = target - 1

        return ans

side, points, k = 2, [[0,2],[2,0],[2,2],[0,0]], 4
side, points, k = 2, [[0,0],[1,2],[2,0],[2,2],[2,1]], 4
side, points, k = 2, [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], 5
side, points, k = 13, [[5,0],[0,3],[9,13],[0,0],[0,13],[10,13]], 4
side, points, k = 76, [[0,2],[25,0],[0,38],[76,53],[0,46]], 4
side, points, k = 16, [[16,8],[0,8],[0,4],[0,14],[4,0],[0,5]], 4
side, points, k = 66, [[0,50],[66,36],[0,9],[5,0],[46,66],[66,23],[0,36]], 4
side, points, k = 65, [[6,0],[0,45],[32,65],[3,65],[20,0],[57,65],[65,39],[0,12]], 4

Solution().maxDistance(side, points, k)