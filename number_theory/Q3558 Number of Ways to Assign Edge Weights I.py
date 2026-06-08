# number theory - medium
from typing import List
from collections import defaultdict
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        MOD = int(1e9 + 7)
        # key ideas:
        # 1) one pass DFS to get max. depth
        # 2) using results of combinatorics to get sum of odd binom. coeff. to be 2^(n-1)
        fmax = lambda a, b: a if a > b else b

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(par:int, curr:int) -> int:
            res = 0
            for neighbour in g[curr]:
                if neighbour != par:
                    res = fmax(res, 1 + dfs(curr, neighbour))
            return res

        maxDepth = dfs(-1, 1)
        return pow(2, maxDepth-1, MOD) 

edges = [[1,2]]
edges = [[1,2],[1,3],[3,4],[3,5]]

Solution().assignEdgeWeights(edges)