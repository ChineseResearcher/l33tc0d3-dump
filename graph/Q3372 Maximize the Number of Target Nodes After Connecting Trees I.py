# graph - medium
from typing import List
from collections import defaultdict, deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        n, m = len(edges1)+1, len(edges2)+1
        # input size for n, m is max. 1000, O(n^2 + m^2) is good enough

        # first build graph for edges1
        g1 = defaultdict(set)
        for a, b in edges1:

            g1[a].add(b)
            g1[b].add(a)

        # build graph for edges2
        g2 = defaultdict(set)
        for u, v in edges2:

            g2[u].add(v)
            g2[v].add(u)

        def build_dist(graph):

            n = len(graph)
            # use bfs/dfs to build the 2-D distance array
            d_cnt = {i: defaultdict(int) for i in range(n)}

            for startNode in range(n):

                visited = set((startNode,))
                # beside the queue, also need to maintain a max. distance tracker
                q, curr_max_dist = deque([[startNode, 0]]), 0
                
                while q:

                    curr, dist = q.popleft()
                    if dist > curr_max_dist:
                        d_cnt[startNode][dist] += d_cnt[startNode][dist-1]
                        curr_max_dist = dist

                    d_cnt[startNode][dist] += 1

                    for neighbour in graph[curr]:
                        if neighbour not in visited:
                            q.append([neighbour, dist+1])
                            visited.add(neighbour)

            return d_cnt

        # dist1[i][j] would represent the number of nodes that are
        # at most j unit-distance away from node i's perspective
        dist1, dist2 = build_dist(g1), build_dist(g2)

        # if one has to draw an additional edge to tree represented by edges2
        # then we query for the best cnt up to distance k-1
        g2_max = 0
        for node_j in range(m):
            max_d2 = max(dist2[node_j].keys())
            if k-1 > max_d2:
                g2_max = max(g2_max, dist2[node_j][max_d2])
            else:
                g2_max = max(g2_max, dist2[node_j][k-1])

        ans = [0] * n
        for node_i in range(n):

            # number of nodes within k distance init. to dist1[node_i][k]
            max_d1 = max(dist1[node_i].keys())
            curr_ans = dist1[node_i][k] if k <= max_d1 else dist1[node_i][max_d1]

            curr_ans += g2_max
            ans[node_i] = curr_ans

        return ans
    
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
k = 2

edges1 = [[0,1],[0,2],[0,3],[0,4]]
edges2 = [[0,1],[1,2],[2,3]]
k = 1

edges1 = [[0,1]]
edges2 = [[0,1],[1,2]]
k = 2

Solution().maxTargetNodes(edges1, edges2, k)