# graph - hard
from typing import List
from collections import deque
import heapq
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        m, n = len(forest), len(forest[0])
        tr = [] # <height, r, c>
        # collect all trees
        for r in range(m):
            for c in range(n):

                if forest[r][c] > 1:
                    tr.append([forest[r][c], r, c])

        tr.sort(key = lambda x: x[0])

        # no trees to cut
        if not tr:
            return 0

        # first cell not "passable"
        if forest[0][0] == 0:
            return -1 

        # ver1: Djikstra's
        def get_sd(r1, c1, r2, c2):

            dist = [ [float('inf')] * n for _ in range(m) ]

            # define directions
            offsets = [(0,1),(0,-1),(1,0),(-1,0)]

            # helper to calculate the shortest distance 
            # given starting coord (r1, c1) to destination coord (r2, c2)
            dist[r1][c1] = 0

            minheap = [(0, r1, c1)] # <curr_dist, r, c>
            while minheap:

                curr_dist, r, c = heapq.heappop(minheap)
                if curr_dist > dist[r][c]:
                    continue

                for dx, dy in offsets:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] != 0:
                    
                        new_dist = curr_dist + 1
                        if nr == r2 and nc == c2:
                            return new_dist

                        if new_dist < dist[nr][nc]:
                            dist[nr][nc] = new_dist
                            
                            heapq.heappush(minheap, (new_dist, nr, nc))

            return float('inf') # unreachable due to blocking '0's

        # ver2: basic BFS
        # have no idea why this runs much faster than above Djikstra's
        def get_sd2(sr, sc, tr, tc):

            if sr == tr and sc == tc:
                return 0

            visited = [ [False] * n for _ in range(m) ]
            queue = deque([(sr, sc, 0)])
            visited[sr][sc] = True

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                r, c, steps = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return steps + 1

                        visited[nr][nc] = True
                        queue.append((nr, nc, steps + 1))

            return float('inf')  # Target is unreachable

        # if (0,0) is not the shortest tree, first add the
        # travel moves needed to get to the shortest
        # note: ALL TREE HEIGHTS ARE UNIQUE (otherwise impossible to solve)
        ans = 0
        if forest[0][0] != tr[0][0]:
            ans += get_sd2(0, 0, tr[0][1], tr[0][2])

        for i in range(len(tr)-1):
            res = get_sd2(tr[i][1], tr[i][2], tr[i+1][1], tr[i+1][2])
            
            if res < float('inf'):
                ans += res
            else:
                return -1

        return ans
    
forest = [[1,2,3],[0,0,4],[7,6,5]]
forest = [[1,2,3],[0,0,0],[7,6,5]]
forest = [[2,3,4],[0,0,5],[8,7,6]]
forest = [[54581641,64080174,24346381,69107959],
          [86374198,61363882,68783324,79706116],
          [668150,92178815,89819108,94701471],
          [83920491,22724204,46281641,47531096],
          [89078499,18904913,25462145,60813308]]

Solution().cutOffTree(forest)