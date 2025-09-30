# graph - hard
from typing import List
from collections import deque, defaultdict
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        if not blocked: return True

        maxVal = int(1e6)
        # shrink the 1 mil x 1 mil grid to only active rols and cols
        activeRow, activeCol = set(), set()

        for r, c in [source] + blocked + [target]:
            
            if r - 1 >= 0:
                activeRow.add(r-1)
            if r + 1 < maxVal:
                activeRow.add(r+1)
            activeRow.add(r)

            if c - 1 >= 0:
                activeCol.add(c-1)
            if c + 1 < maxVal:
                activeCol.add(c+1)
            activeCol.add(c)

        # make blocked set
        temp = set()
        for r, c in blocked:
            temp.add((r, c))
        blocked = temp

        # build neighbouring rows and cols
        ar, ac = sorted(activeRow), sorted(activeCol)
        nr, nc = defaultdict(list), defaultdict(list)

        m = len(ar)
        for i in range(m):
            if i - 1 >= 0:
                nr[ar[i]].append(ar[i-1])
            if i + 1 < m:
                nr[ar[i]].append(ar[i+1])

        n = len(ac)
        for j in range(n):
            if j - 1 >= 0:
                nc[ac[j]].append(ac[j-1])
            if j + 1 < n:
                nc[ac[j]].append(ac[j+1])

        # use BFS to traverse the grid
        q, visited = deque([source]), set((tuple(source),))
        while q:

            r, c = q.popleft()
            if [r, c] == target:
                return True

            # find row-wise neighbour
            for neighbour in nr[r]:
                if (neighbour, c) not in visited and (neighbour, c) not in blocked:
                    q.append([neighbour, c])
                    visited.add((neighbour, c))

            # find col-wise neighbour
            for neighbour in nc[c]:
                if (r, neighbour) not in visited and (r, neighbour) not in blocked:
                    q.append([r, neighbour])
                    visited.add((r, neighbour))

        return False
    
blocked, source, target = [[0,1],[1,0]], [0,0], [0,2]
blocked, source, target = [], [0,0], [999999,999999]
# constraint
import random
blocked, source, target = [[random.randint(0, int(1e6)), random.randint(0, int(1e6))] for _ in range(200)], [0,0], [999999,999999]

Solution().isEscapePossible(blocked, source, target)