# dp - hard
from typing import List
from functools import cache
from collections import defaultdict

# heuristic O(n^3*2^n)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        # key ideas:
        # 1) for a connected graph, which has n*(n-1) edges if fully connected,
        # it takes at worst n^2 edge visits to visit all nodes at least once

        # 2) we can formulate our top-down DP problem as f(k, mask, x), which returns
        # True / False if we can visit all nodes at least once in "k" steps, ending
        # at node "x" and with a visited state mask

        # 3) since n is small (n <= 12), we can use a heuristic approach to find out
        # the smallest "k" that returns True for x in range [0, n-1]

        g = defaultdict(list)
        for u in range(n):
            for v in graph[u]:
                g[u].append(v)

        @cache
        def f(k: int, mask: int, x: int) -> bool:

            # moves exhausted
            if k == 0:
                return True if mask == (1 << x) else False
            
            # subproblems:
            # 1) reach neighbour i in k-1 steps, with x not visited
            # 2) reach neighbour i in k-1 steps, with x already visited
            for i in g[x]:
                if f(k-1, mask & ~(1 << x), i):
                    return True
                if f(k-1, mask, i):
                    return True
                
            return False

        k, FINAL = 0, (1 << n) - 1
        while True:
            for x in range(n):
                if f(k, FINAL, x):
                    return k # smallest steps needed
            k += 1

# Floyd-Warshall + DP (O(n^3 + n^2*2^n))
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)
        dist = [ [float('inf')] * n for _ in range(n) ]

        for i in range(n):
            dist[i][i] = 0
        for u in range(n):
            for v in graph[u]:
                dist[u][v] = 1

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        FINAL = (1 << n) - 1
        @cache
        def f(mask: int, idx: int) -> int:
            if mask == FINAL:
                return 0

            res = float('inf')
            for i in range(n):
                # find next unvisited node
                if not mask & (1 << i):
                    # directly access min. pairwise distance computed by Floyd
                    res = min(res, (dist[idx][i] if idx != -1 else 0) + \
                                    f(mask | (1 << i), i))

            return res

        return f(0, -1)
    
graph = [[1,2,3],[0],[0],[0]]
graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]

Solution().shortestPathLength(graph)