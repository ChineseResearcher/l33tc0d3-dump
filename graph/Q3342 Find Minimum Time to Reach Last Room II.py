# graph - medium
from typing import List
from collections import deque
import bisect
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        # the spirit of Djikstra's is that when we reach a node,
        # it's guaranteed to be the shortest path leading up to this node
        m, n = len(moveTime), len(moveTime[0])

        # maintain a 2-D arr. to indicate visited
        visited = [[False] * n for _ in range(m)]

        # offsets to visit adjacent cells
        offsets = [(1,0),(-1,0),(0,1),(0,-1)]

        # stack stores <currTime, row, col, timeCostForThisRound>
        dq = deque([[0,0,0,1]])
        visited[0][0] = True
        while dq:

            t, r, c, dt = dq.popleft()
            for dr, dc in offsets:

                nr, nc = r + dr, c + dc
                # validate neighbour
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    nt = max(moveTime[nr][nc], t) + dt
                    if nr == m-1 and nc == n-1:
                        return nt

                    next_entry = [nt, nr, nc, 3 - dt] # alternate crossing time
                    iidx = bisect.bisect_left(dq, next_entry)

                    # insert into deque at sorted pos.
                    dq.insert(iidx, next_entry)

                    # mark visited
                    visited[nr][nc] = True

moveTime = [[0,4],[4,4]]
moveTime = [[0,0,0,0],[0,0,0,0]]
moveTime = [[0,1],[1,2]]

Solution().minTimeToReach(moveTime)