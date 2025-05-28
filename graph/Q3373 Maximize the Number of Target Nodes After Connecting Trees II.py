# graph - hard
from typing import List
from collections import defaultdict, deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
        n, m = len(edges1), len(edges2)
        # similar to iteration I, we build a tree graph for g1 & g2
        def build_graph(e):

            g = defaultdict(set)
            for u, v in e:
                g[u].add(v)
                g[v].add(u)

            return g

        g1, g2 = build_graph(edges1), build_graph(edges2)

        # now realise that if we root both g1 & g2 at node 0, and that 
        # we perform one bfs traversal for each, then the distance between
        # even-distanced nodes is even, similarly for odd-distanced nodes
        def bfs(g):

            level_cnt, grouping = defaultdict(int), dict()
            # notice that a tree does not contain cycle, so we only
            # need to track parent to avoid re-visiting
            q = deque([[0, 0, -1]])
            while q:

                node, dist, parent = q.popleft()

                # record traversal 
                level_cnt[dist] += 1
                grouping[node] = dist

                for neighbour in g[node]:
                    if neighbour != parent:
                        q.append([neighbour, dist+1, node])

            return level_cnt, grouping

        lc1, gp1 = bfs(g1)
        lc2, gp2 = bfs(g2)

        # obtain the even-level & odd-level counts for both g1 & g2
        def tab(lc):

            even_cnt, odd_cnt = 0, 0
            for lvl, cnt in lc.items():
                if lvl % 2 == 0:
                    even_cnt += cnt
                else:
                    odd_cnt += cnt

            return even_cnt, odd_cnt

        e1c, o1c = tab(lc1)
        e2c, o2c = tab(lc2)

        ans = [0] * (n+1)
        for node in range(n+1):

            # determine the node's level parity
            if gp1[node] % 2 == 0:
                ans[node] += e1c
            else:
                ans[node] += o1c

            ans[node] += max(e2c, o2c)

        return ans
    
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

edges1 = [[0,1],[0,2],[0,3],[0,4]]
edges2 = [[0,1],[1,2],[2,3]]

Solution().maxTargetNodes(edges1, edges2)