# graph - medium
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times, n, k):
        
        # an application of Dijkstra's, we are supposed to find the
        # min. dist/time for signal to reach from node k to all nodes
        graph = defaultdict(list)
        for u, v, w in times:

            # directed edges, change to 0-indexing
            graph[u-1].append((v-1,w))

        delay = [float('inf')] * n
        delay[k-1] = 0

        min_heap = [[0, k-1]]
        while min_heap:

            cumu_delay, curr_node = heapq.heappop(min_heap)
            # skip outdated path
            if cumu_delay > delay[curr_node]:
                continue

            # otherwise, explore neighbours
            for neighbour, d in graph[curr_node]:
                new_delay = cumu_delay + d
                if new_delay < delay[neighbour]:
                    delay[neighbour] = new_delay
                    heapq.heappush(min_heap, [new_delay, neighbour])

        minTime = max(delay)
        return minTime if minTime < float('inf') else -1
    
times, n, k = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
times, n, k = [[1,2,1]], 2, 1
times, n, k = [[1,2,1]], 2, 2

Solution().networkDelayTime(times, n, k)