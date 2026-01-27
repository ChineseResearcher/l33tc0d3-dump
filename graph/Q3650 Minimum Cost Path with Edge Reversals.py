# graph - medium
import heapq
from collections import defaultdict
from typing import List
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        # build a normal and reverse graph
        G = defaultdict(list)
        reverseG = defaultdict(list)
        for u, v, w in edges:
            G[u].append((v, w))
            reverseG[v].append((u, w))

        # Dijistra's minheap, dist
        minheap = [(0, 0)] # <acc_cost, curr_node>
        dist = [float('inf')] * n
        dist[0] = 0

        # another boolean array to indicate reverse status
        rev = [False] * n

        # traversal from 0 to n-1
        while minheap:

            acc_dist, curr = heapq.heappop(minheap)
            if acc_dist > dist[curr]:
                continue

            for neighbour, w in G[curr]:
                new_dist = acc_dist + w
                if new_dist < dist[neighbour]:
                    dist[neighbour] = new_dist
                    heapq.heappush(minheap, (new_dist, neighbour))

            if not rev[curr]:
                rev[curr] = True
                for neighbour, w in reverseG[curr]:
                    new_dist = acc_dist + 2 * w
                    if new_dist < dist[neighbour]:
                        dist[neighbour] = new_dist
                        heapq.heappush(minheap, (new_dist, neighbour))

        return dist[n-1] if dist[n-1] < float('inf') else -1
    
n, edges = 4, [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
n, edges = 4, [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
n, edges = 4, [[2,3,25],[2,1,18],[3,1,2]]

Solution().minCost(n, edges)