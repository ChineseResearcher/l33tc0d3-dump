# graph - medium
from typing import List
from collections import deque, defaultdict
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n = len(classroom), len(classroom[0])
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) use BFS to find min. moves required
        # 2) track a bitmask to indicate the picked up letter(s)
        # 3) prune BFS by maintaining bestEnergy[r][c][mask], where we do not revisit
        # a cell if curr. energy is smaller than the best recorded

        r0, c0, L = -1, -1, dict()
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    r0, c0 = r, c
                # create mapping to bitmask
                if classroom[r][c] == 'L':
                    L[(r, c)] = len(L)

        bestEnergy = defaultdict(lambda: -1)
        # pos, curr. energy level, cumulative dist., mask of collected litter cnt
        q = deque([(r0, c0, energy, 0, 0)]) 
        while q:

            r, c, e, d, k = q.popleft()
            if k.bit_count() == len(L):
                return d
            
            # no energy, terminate
            if e == 0: continue

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:

                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:

                    nchar, ne, nk = classroom[nr][nc], e - 1, k
                    # skip obstacles
                    if nchar == 'X':
                        continue
                    elif nchar == 'R':
                        ne = energy
                    elif nchar == 'L':
                        nk = k | (1 << (L[(nr, nc)]))

                    # skip visited cells if curr. energy level is not strictly better
                    if ne <= bestEnergy[(nr, nc, nk)]: continue
                    bestEnergy[(nr, nc, nk)] = fmax(bestEnergy[(nr, nc, nk)], ne)
                    q.append((nr, nc, ne, d + 1, nk))

        return -1

classroom, energy = ["S.", "XL"], 2
classroom, energy = ["LS", "RL"], 4
classroom, energy = ["LS", "L."], 3
classroom, energy = ["RL", "S."], 1
classroom, energy = ["L.S", "RXL"], 3

Solution().minMoves(classroom, energy)