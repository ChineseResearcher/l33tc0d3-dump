# geometry - hard
import math
from typing import Tuple, List
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
        if len(trees) == 1:
            return trees
        # key ideas:
        # 1) the problem is equivalent to finding the convex hull of given coordinates
        # 2) at any outermost point, the next outermost point is determined by an
        # anti-clockwise scan w/ the remaining points s.t. it has the least angle deg
        # 3) we start at the bottom-left-most point where the anti-clockwise 
        # field of view is starting at 0 deg east
        coords = set()
        for x, y in trees:
            coords.add((x,y))

        # track the bottom-left-most point
        trees.sort(key=lambda x: (x[1], x[0]))
        startingPt = tuple(trees[0])

        def angle_deg(ref: Tuple[float, float], pt: Tuple[float, float]) -> float:
            """
            Compute a compass-like angle in degrees in [0, 360):
            - 0° points to +x (East)
            - 90° points to +y (North)
            - 180° points to -x (West)
            - 270° points to -y (South)
            Returns float; SW lies in (180, 270).
            """
            dx = pt[0] - ref[0]
            dy = pt[1] - ref[1]
            # perform gcd reduction
            g = math.gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g

            ang = math.degrees(math.atan2(dy, dx))
            return (ang + 360.0) % 360.0

        def euc_dist2(ref: Tuple[float, float], pt: Tuple[float, float]) -> float:
            return pow(pt[0]-ref[0], 2) + pow(pt[1]-ref[1], 2)

        # init. a boolean loop to indicate we have started the convex hull search
        loop = False

        # init. reference coord to startingPt
        ref = startingPt

        # track the previous min. angle
        prev_min_angle = 0

        ans = [startingPt]
        while True:

            if loop and ref == startingPt:
                ans.pop()
                break

            min_angle, min_dist, next_ref = float('inf'), float('inf'), None
            for x, y in coords:
                if (x, y) != ref:
                    angle, dist = angle_deg(ref, (x,y)), euc_dist2(ref, (x,y))
                    if angle >= prev_min_angle:
                        if angle < min_angle:
                            min_angle = angle
                            # reset min_dist
                            min_dist = dist
                            next_ref = (x, y)
                        elif angle == min_angle:
                            # same angle break tie by smaller dist
                            if dist < min_dist:
                                min_dist = dist
                                next_ref = (x, y)
            
            ans.append(next_ref)
            # remove the curr. coord from search space as long
            # as it's not the starting point
            if ref != startingPt:
                coords.discard(ref)

            # update prev. min. angle
            prev_min_angle = min_angle
            # update ref
            ref = next_ref
            loop = True

        return ans

trees = [[1,2],[2,2],[4,2]]
trees = [[0,5],[10,0],[10,10],[0,10],[0,0]]
trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]

Solution().outerTrees(trees)