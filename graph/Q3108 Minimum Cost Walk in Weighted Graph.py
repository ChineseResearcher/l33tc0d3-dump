# graph - hard
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
    def minimumCost(self, n: int, edges, query):
        
        # graph is unweighted and may contain cycles, and it
        # is designed in such a way that the best optimal route
        # between two nodes can involve revisiting same nodes

        # as the cost of path is the bitwise & of all weights
        # in the path, the nice property that bitwise & only 
        # remains same OR reduces is the key idea to solving this

        # the cost of the optimal path between any two nodes
        # is thus the bitwise & of all the weights in the connected
        # component that both node A and node B belong to

        # construct DSU of size n
        uf = UnionFind(n)

        # process all edges and union nodes connected by an edge
        for u, v, _ in edges:
            uf.union(u, v)

        cluster_weights = defaultdict(list)
        # another pass through edges list to add edge weights to 
        # all the connected components respectively identified by its parent
        for u, v, w in edges:
            
            # make sure u, v have been pointed to the same parent
            _, _ = uf.find(u), uf.find(v)
            parent = uf.parent[u]
            cluster_weights[parent].append(w)

        cluster_bitwiseAND = defaultdict(int)
        # compute the bitwise & of all components (group with > 1 member)
        for p, weights in cluster_weights.items():

            res = None
            for w in weights:
                if res is None:
                    res = w
                else:
                    res = res & w
            cluster_bitwiseAND[p] = res

        ans = []
        for u, v in query:

            if uf.connected(u, v):
                ans.append(cluster_bitwiseAND[uf.parent[u]])
            else:
                ans.append(-1)

        return ans
    
n, edges, query = 3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]
n, edges, query = 5, [[0,1,7],[1,3,7],[1,2,1]], [[0,3],[3,4]]
n, edges, query = 7, [[2,5,7],[0,4,14],[1,5,0],[0,1,7],[4,5,10]], [[4,5],[4,1]]

Solution().minimumCost(n, edges, query)