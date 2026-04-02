# simulation - medium
from typing import List
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        fmax = lambda a, b: a if a > b else b
        # define useful constants
        body_pos = [0,1,2,3] # north, east, south, west
        delta = [(0,1),(1,0),(0,-1),(-1,0)]

        # use a hashset to record obstacles
        b = set([(r, c) for r, c in obstacles])

        # euc. dist. helper
        euc_dist = lambda r, c: pow(r, 2) + pow(c, 2)

        r, c, p, ans = 0, 0, 0, 0
        for x in commands:
            # turn left
            if x == -2:
                p = (p - 1 + 4) % 4
                continue
            # turn right
            if x == -1:
                p = (p + 1 + 4) % 4
                continue

            dr, dc = delta[p][0], delta[p][1]
            for _ in range(x):
                nr, nc = r + dr, c + dc
                if (nr, nc) in b:
                    break
                # implement the move
                r, c = nr, nc
                ans = fmax(ans, euc_dist(r, c))

        return ans
    
commands, obstacles = [4,-1,3], []
commands, obstacles = [4,-1,4,-2,4], [[2,4]]
commands, obstacles = [6,-1,-1,6], [[0,0]]

Solution().robotSim(commands, obstacles)