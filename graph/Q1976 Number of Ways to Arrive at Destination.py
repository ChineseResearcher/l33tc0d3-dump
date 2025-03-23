# graph - medium
from collections import defaultdict
import heapq # for PQ-based Dijkstra's

class Solution:
    def countPaths(self, n, roads):
        
        # this question is very difficult to get the right approach
        # with rating at 2000+, a simple Dijkstra's would not work

        # first subproblem is to find the edges that are involved in
        # the shortest path (SP) up to node i, mathematically, we want to
        # find all weighted_edge s.t. dist[u] + weighted_edge = dist[v]
        # where dist[x] stores the shortest distance from node 0 to x
        road_edges = defaultdict(list)
        dist = [float('inf')] * n
        dist[0] = 0

        # build bi-didrectional edges with weights
        for u, v, w in roads:

            road_edges[u].append((v, w))
            road_edges[v].append((u, w))

        min_heap = [(0, 0)]
        # use Dijkstra's to compute the shortest distance from 0 to each node i
        while min_heap:

            cumu_dist, curr_node = heapq.heappop(min_heap)
            for neighbour, weight in road_edges[curr_node]:
                new_dist = cumu_dist + weight
                # not strictly smaller because there can
                # be multiple shortest path up to X of the same cumu_dist
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbour))

        dag_edges = defaultdict(set)
        # now we collect those edges that are part of the optimal SPs
        for u, v, w in roads:
            if dist[u] + w == dist[v]:
                dag_edges[u].add(v)
            elif dist[v] + w == dist[u]:
                dag_edges[v].add(u)

        # with the derived DAG we could obtain a topological ordering of nodes 
        # involved in the shortest path(s) from node 0 to node N
        dfs_visited = set()
        dfs_stack = []

        # dfs-based topoSort
        def dfs(node):

            if node not in dfs_visited:
                for neighbor in dag_edges[node]:
                    dfs(neighbor)
                dfs_visited.add(node)
                dfs_stack.append(node)

        # starting dfs from source 0
        dfs(0)
        # correct order by reversing the stack
        dfs_stack = dfs_stack[::-1]

        m = len(dfs_stack)
        # solve the problem by O(m^2) DP
        dp = [0] * m
        dp[0] = 1

        for i in range(1, m):
            for j in range(i):
                # check if a directed j -> i edge already
                # existed in our collected desired set
                if dfs_stack[i] in dag_edges[dfs_stack[j]]:
                    dp[i] += dp[j]
                    dp[i] %= int(1e9 + 7)

        # node N could appear anywhere in the topological order
        return dp[dfs_stack.index(n-1)]
            