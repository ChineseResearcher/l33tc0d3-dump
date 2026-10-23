# graph - medium
import heapq
from collections import defaultdict
class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:

        # key ideas:
        # 1) implement SP algo but with additional states tracking prev. letter,
        # and the cumulative count of the letter (i.e. it resets to 1 if curr. differs)
        # 2) track the best dist. for states (node, k) where k indicates the consecutive
        # identical char. count including char. at the node

        g = defaultdict(list)
        for u, v, c in edges:
            g[u].append((v, c)) # edge is directed, so cost can be diff. 

        d = [ [float('inf')] * (k + 1) for _ in range(n) ]
        pq = [(0, 0, labels[0], 1)]
        d[0][1] = 0

        while pq:

            cost, node, char, cnt = heapq.heappop(pq)
            # less optimal than existing best
            if cost > d[node][cnt]:
                continue

            if node == n - 1:
                continue

            for u, w in g[node]:
                if labels[u] != labels[node]:
                    newChar, newCnt = labels[u], 1
                else:
                    newChar, newCnt = char, cnt + 1

                # violate max consecutive cnt allowed
                if newCnt > k:
                    continue

                newCost = cost + w
                if newCost < d[u][newCnt]:
                    heapq.heappush(pq, (newCost, u, newChar, newCnt))
                    d[u][newCnt] = newCost

        minW = min(d[n - 1])
        return minW if minW < float('inf') else -1

n, edges, labels, k = 3, [[0,1,1],[1,2,1]], "aaa", 2
n, edges, labels, k = 2, [[0,1,9817],[1,0,7215]], "pm", 1
n, edges, labels, k = 3, [[0,1,1],[1,2,1],[0,2,3]], "aab", 1
n, edges, labels, k = 3, [[0,1,1],[1,2,1],[0,2,3]], "aab", 2

Solution().shortestPath(n, edges, labels, k)