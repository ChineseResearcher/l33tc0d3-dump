# graph - medium
class UnionFind:
    def __init__(self, n):
        # Initialize the Union-Find structure with n elements
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [1] * n           # Rank is used for union by rank

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
    def findRedundantConnection(self, edges):
        n = max(sum(edges, []))

        # underlying idea is to make use of the concept of a Disjoint Set Union (DSU) or Union Find
        # thus we need a parent array indicating which group a node belongs to
        uf = UnionFind(n+1)

        for n1, n2 in edges:

            # check if they are already under the same parent, if yes
            # that's the (final) additional edge that causes a cycle
            if uf.connected(n1, n2):
                return [n1, n2]

            # otherwise merge n1 & n2
            uf.union(n1, n2)

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
edges = [[1,2],[1,3],[2,3]]
edges = [[1,3],[3,4],[1,5],[3,5],[2,3]]
edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
edges = [[1,5],[3,4],[3,5],[4,5],[2,4]] # this TC is import to understand why a full UF implementation is needed

Solution().findRedundantConnection(edges)