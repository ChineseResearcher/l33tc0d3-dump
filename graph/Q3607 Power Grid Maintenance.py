# graph - medium
import heapq
from typing import List
class UnionFind:
    def __init__(self, n):
        # Initialize the Union-Find structure with n elements
        self.parent = list(range(n))  
        self.rank = [1] * n           

    def find(self, x):
        # Find with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        # construct a DSU based on UnionFind class with "c" stations
        dsu = UnionFind(c+1)

        for u, v in connections:
            dsu.union(u, v)

        # run dsu.find again to make sure compression is applied to all
        for station in range(1, c+1):
            dsu.find(station)

        # construct a mapping where the root of each cluster is the key
        # and we build a minheap of stations in the cluster
        c_map = dict()

        for station in range(1, c+1):
            c_root = dsu.parent[station]
            if c_root not in c_map:
                c_map[c_root] = [station]
            else:
                heapq.heappush(c_map[c_root], station)

        ans, disabled = [], [False] * (c + 1)
        for q_type, station in queries:

            # query for station x
            if q_type == 1:

                root = dsu.parent[station]
                # station itself is still operational
                if not disabled[station]:
                    ans.append(station)
                    continue

                # otherwise, we need to find the smallest operational station
                # note: lazy-delete the already disabled stations
                while c_map[root] and disabled[c_map[root][0]]:
                    heapq.heappop(c_map[root])

                # no operational stations in the cluster at all
                if not c_map[root]:
                    ans.append(-1)
                    continue

                ans.append(c_map[root][0]) # smallest of heap
                 
            # disable operation for station x
            else:
                disabled[station] = True

        return ans
    
c, connections, queries = 5, [[2,3],[3,4],[4,5],[1,2]], [[1,3],[2,1],[1,1],[2,2],[1,2]]
c, connections, queries = 3, [], [[1,1],[2,1],[1,1]]

Solution().processQueries(c, connections, queries)