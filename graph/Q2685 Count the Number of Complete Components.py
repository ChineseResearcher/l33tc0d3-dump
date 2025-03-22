# graph - medium
from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        # Initialize the Union-Find structure with n elements
        self.parent = list(range(n))  
        self.rank = [1] * n     

    def find(self, x):
        # Find with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
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
                self.rank[root_x] += 1  # Increase rank when merging equal-rank trees

    def connected(self, x, y):
        # Check if two elements are in the same set
        # Note: this is the key to validating a cycle
        return self.find(x) == self.find(y)

class Solution:
    def countCompleteComponents(self, n, edges):
        # construct DSU of size n
        uf = UnionFind(n)

        # for all edges, union them as we process
        for u,v in edges:
            uf.union(u,v)

        # construct two dicts
        # first dict stores the set of nodes in a component
        # second dict stores the count of edges in a component
        cluster_nodes = defaultdict(set)
        cluster_edge_cnt = defaultdict(int)

        for u,v in edges:

            # make sure u, v points to the same cluster parent
            _, _ = uf.find(u), uf.find(v)
            parent = uf.parent[u]

            cluster_nodes[parent].add(u)
            cluster_nodes[parent].add(v)

            cluster_edge_cnt[parent] += 1

        # for each unique cluster parent (ucp), check if its 
        # egde cnt = nCk, where k is the number of nodes in this cluster
        ans = 0
        for ucp in set(uf.parent):

            nodesCnt = len(cluster_nodes[ucp])
            if cluster_edge_cnt[ucp] == nodesCnt * (nodesCnt-1) // 2:
                ans += 1

        return ans
    
n, edges = 6, [[0,1],[0,2],[1,2],[3,4]]
n, edges = 6, [[0,1],[0,2],[1,2],[3,4],[3,5]]

Solution().countCompleteComponents(n, edges)