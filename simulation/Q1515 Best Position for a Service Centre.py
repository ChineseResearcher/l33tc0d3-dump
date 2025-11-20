# simulation - hard
import math
from typing import List
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        
        # key ideas:
        # 1) it can be mathematically proven that the sum of euclidean distances in 2D is convex
        # 2) since target function is convex, we can iteratively descend to the global minimum
        # 3) since it's 2D, we could explore cardinal directions in the descent

        # minimum threshold for a "step"
        EPS = 1e-7 
        step = 1

        n = len(positions)
        # we start off with mean of x and mean of y
        x = sum(p[0] for p in positions) / n
        y = sum(p[1] for p in positions) / n

        # define a helper to help us compute the total sum of dist
        # if p0 is chosen as the solution coordinate
        cost = lambda p0: sum(math.dist(p0, p) for p in positions)

        while step > EPS:

            curr_cost, desc = cost((x,y)), False
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:

                nx, ny = x + step * dx, y + step * dy
                if cost((nx, ny)) < curr_cost:
                    x, y = nx, ny
                    desc = True
                    break
            
            # in the case we did not successfully descend
            if not desc:
                # adjust down the step size as we might have 
                # "overshoot" the move which then misses the decrement
                step *= 0.5

        # answer based on final updated (x,y)
        return cost((x, y))

positions = [[1,1]]
positions = [[1,1],[3,3]]
positions = [[58,32],[41,21]]
positions = [[1,1],[0,0],[2,0]]
positions = [[0,1],[1,0],[1,2],[2,1]]
positions = [[44,23],[18,45],[6,73],[0,76],[10,50],[30,7],[92,59],
             [44,59],[79,45],[69,37],[66,63],[10,78],[88,80],[44,87]]

Solution().getMinDistSum(positions)