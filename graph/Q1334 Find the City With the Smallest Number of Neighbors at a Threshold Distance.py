# graph - medium
import heapq
from typing import List
from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # key ideas:
        # 1) we can use either Floyd-Warshall or Djikstra's for this problem
        # 2) for Djikstra's, perform search for every source node

        g = defaultdict(list)
        for u, v, d in edges:
            g[u].append((v, d))
            g[v].append((u, d))

        def djikstra(source:int, threshold:int) -> int:
            '''
            Run Djikstra's algo and obtain the count of cities
            that are within threshold distance from source city
            '''

            dist = [float('inf')] * n
            dist[source] = 0

            pq = [(source, 0)]
            while pq:

                i, d = heapq.heappop(pq)
                if d > dist[i]:
                    continue

                if d > threshold:
                    continue

                for j, nd in g[i]:
                    if d + nd < dist[j]:
                        dist[j] = d + nd
                        heapq.heappush(pq, (j, d + nd))

            return len([d for d in dist if 0 < d <= threshold])

        res = [(djikstra(i, distanceThreshold), i) for i in range(n)]
        # smallest count -> largest city name
        res.sort(key=lambda x: (x[0], -x[1]))

        return res[0][1]

n, edges, distanceThreshold = 4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4
n, edges, distanceThreshold = 5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2
n, edges, distanceThreshold = 6, [[0,3,5],[2,3,7],[0,5,2],[0,2,5],[1,2,6],[1,4,7],[3,4,4],[2,5,5],[1,5,8]], 8279

Solution().findTheCity(n, edges, distanceThreshold)