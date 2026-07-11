# graph - medium
from typing import Tuple, List
from collections import deque, defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # key ideas:
        # 1) BFS discovery of components, track nodeCnt / edgeCnt
        # 2) validate "completeness“ with formula

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def bfs(source:int) -> Tuple[set, int]:
            '''
            BFS helper to determine the node / edge cnt of curr. component
            with "source" as the starting node.
            '''
            q = deque([source])

            vNodes, vEdges = set([source]), set()
            while q:

                curr = q.popleft()
                for nxt in g[curr]:
                    a, b = curr, nxt
                    if a > b: a, b = b, a
                    vEdges.add((a, b))

                    if nxt not in vNodes:
                        q.append(nxt)
                        vNodes.add(nxt)

            return vNodes, len(vEdges)

        # global visited node set
        v, ans = set(), 0
        for node in range(n):
            if node not in v:
                vNodes, edgeCnt = bfs(node)
                nodeCnt = len(vNodes)
                # validate
                if edgeCnt == nodeCnt * (nodeCnt - 1) // 2:
                    ans += 1
                # merge visited
                v |= vNodes

        return ans
    
n, edges = 6, [[0,1],[0,2],[1,2],[3,4]]
n, edges = 6, [[0,1],[0,2],[1,2],[3,4],[3,5]]

Solution().countCompleteComponents(n, edges)