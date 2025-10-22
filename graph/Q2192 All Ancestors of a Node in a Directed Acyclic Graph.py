# graph - medium
from typing import List
from collections import defaultdict, deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # BFS-based topoSort
        inDeg = defaultdict(int)
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            inDeg[v] += 1

        q = deque()
        # collect all nodes with inDeg = 0
        for node in range(n):
            if inDeg[node] == 0:
                q.append(node)

        ans = [ set() for _ in range(n) ]
        while q:

            curr = q.popleft()
            for neighbour in g[curr]:

                # mark ancestor
                ans[neighbour].add(curr)
                ans[neighbour] |= ans[curr]
                inDeg[neighbour] -= 1

                if inDeg[neighbour] == 0:
                    q.append(neighbour)

        return [sorted(list(x)) for x in ans]
    
n, edgeList = 8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
n, edgeList = 5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Solution().getAncestors(n, edgeList)