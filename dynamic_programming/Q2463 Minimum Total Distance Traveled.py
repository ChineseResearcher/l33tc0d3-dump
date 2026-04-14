# dp - hard
from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        # key ideas:
        # 1) first sort the robot and factory arrays, and unpack factory array
        # 2) solve a knapsack DP concerning robots and unpacked factories

        robot.sort()
        factory.sort(key=lambda x: x[0])

        # flatten factory positions according to their capacities
        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                # e.g. [2,3] becomes [2,2,2] 
                factory_positions.append(f[0])

        # note: there are at most 100 factories with each factory's repair limit up to 100
        # by building a 2D dp concerning length of robots and factory_positions
        # we will have maximum dimensions of 100 * (100 * 100) = 100 * 10000
        m, n = len(factory_positions), len(robot)

        dp = [ [float('inf')] * (n+1) for _ in range(m+1) ]
        # when there's no robot to fix, total dist is 0
        for i in range(m+1):
            dp[i][0] = 0

        for i in range(1, m+1):
            for j in range(1, min(i+1,n+1)):
                
                # pair this j-th robot with the i-th factory
                assign = abs(robot[j-1]-factory_positions[i-1]) + dp[i-1][j-1]

                # skip the curr. factory
                skip = dp[i-1][j]

                dp[i][j] = min(assign, skip)

        return dp[-1][-1]

robot, factory = [0,4,6], [[2,2],[6,2]]
robot, factory = [1,-1], [[-2,1],[2,1]]
robot, factory = [9,11,99,101], [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]

Solution().minimumTotalDistance(robot, factory)