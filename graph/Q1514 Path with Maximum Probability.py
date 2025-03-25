# graph - medium
from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        
        m = len(edges)
        # classic Dijkstra's problem, except that instead of min-heap
        # a max-heap is used because it wants path with max. proba
        graph = defaultdict(list)

        for i in range(m):

            u, v = edges[i][0], edges[i][1]
            proba = succProb[i]

            # undirected edges
            graph[u].append((v, proba))
            graph[v].append((u, proba))

        max_heap = [[-1, start_node]]
        # similar to dist arr.
        proba = [0] * n
        proba[start_node] = 1

        while max_heap:

            cumu_proba, curr_node = heapq.heappop(max_heap)
            # skip outdated path
            if abs(cumu_proba) < proba[curr_node]:
                continue

            # otherwise, explore neighbours
            for neighbour, p in graph[curr_node]:
                new_proba = abs(cumu_proba) * p

                # only update if better option with higher proba is found
                if new_proba > proba[neighbour]:
                    proba[neighbour] = new_proba
                    heapq.heappush(max_heap, [-new_proba, neighbour])

        return proba[end_node] 
    
n, edges, succProb, start_node, end_node = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2
n, edges, succProb, start_node, end_node = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2
n, edges, succProb, start_node, end_node = 3, [[0,1]], [0.5], 0, 2

Solution().maxProbability(n, edges, succProb, start_node, end_node)