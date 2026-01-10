# binary search - hard
from collections import defaultdict, deque
from typing import List
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:

        n = len(points)
        # special case: only two points, define partition factor to be 0 only
        if n == 2:
            return 0

        def bfs(g:defaultdict) -> bool:

            # bfs traversal to determine if the graph is bipartite
            # note:
            # 1) given the property of a bipartite graph, every node can be
            # colored either 0/1, to indicate proper grouping into 2
            # 2) we use states array to be initiated to all -1 (unvisited)
            # and subsequently 0/1 depending on coloring
            states = {node:-1 for node in g}

            bipartite = True
            for node in states.keys():
                # there may still be unvisited nodes after one round of BFS
                if states[node] == -1:

                    q = deque([node])
                    states[node] = 0
                    while q:

                        curr = q.popleft()
                        for neighbour in g[curr]:

                            if states[neighbour] != -1:
                                # conflict of 2-colouring
                                if states[curr] == states[neighbour]:
                                    bipartite = False
                                    break

                            else: 
                                q.append(neighbour)
                                states[neighbour] = 1 - states[curr]

                        if not bipartite:
                            break # early stop

                    if not bipartite:
                        break

            return bipartite

        # binary search checker on target Manhattan dist
        def target_is_valid(target:int) -> bool:

            g = defaultdict(set)
            # explore all pairs to obtain edges
            for i in range(n):
                for j in range(n):

                    if i == j:
                        continue

                    if dist[i][j] < target:
                        g[i].add(j)
                        g[j].add(i)

            # if there's not a single failed pair (no edge)
            # then we consider target feasible
            if len(g) == 0:
                return True
            
            return bfs(g)

        dist = [ [-1] * n for _ in range(n) ]
        fmax = lambda a, b: a if a > b else b
        # our goal is to establish the correct right bound
        # in the meantime, compute the distance between every unique pair
        r = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                dist[i][j] = abs(points[i][0]-points[j][0]) + \
                             abs(points[i][1]-points[j][1])
                dist[j][i] = dist[i][j]
                r = fmax(r, dist[i][j])

        l = 0
        while l <= r:

            mid = (l + r) // 2
            if target_is_valid(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r

points = [[0,0],[0,2],[2,0],[2,2]]
points = [[0,0],[0,1],[10,0]]
points = [[0,0],[0,0],[0,0]]
points = [[-82957,77541],[15697,31252],[99010,73696],[58710,26593],[-60460,99184]]

Solution().maxPartitionFactor(points)