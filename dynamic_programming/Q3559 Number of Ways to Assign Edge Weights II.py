# dp - hard
from collections import defaultdict
class TreeDistance:
    def __init__(self, graph, n, root=1):
        """
        Initialize with:
        - graph: defaultdict(list) representing adjacency list with (neighbor, weight)
        - n: number of nodes
        - root: starting node for preprocessing
        """
        self.graph = graph
        self.n = n
        self.root = root
        self.LOG = (n).bit_length()  # max power for binary lifting
        # DP table: up[node][j] = 2^j-th ancestor of node
        self.up = [[-1] * self.LOG for _ in range(n + 1)]
        self.depth = [0] * (n + 1)
        self.dist = [0] * (n + 1)
        self._preprocess()

    def _dfs(self, node, parent):
        """
        DFS to compute:
        - depth[node]
        - dist[node]
        - Fill DP table for binary lifting:
          up[node][j] = up[ up[node][j-1] ][j-1]
          This is the core DP relation:
          If we know the 2^(j-1)-th ancestor, then the 2^j-th ancestor
          is the ancestor of that ancestor.
        """
        for v, w in self.graph[node]:
            if v == parent:
                continue
            self.depth[v] = self.depth[node] + 1
            self.dist[v] = self.dist[node] + w
            self.up[v][0] = node  # base case for DP: immediate parent
            # Build DP table for v:
            for j in range(1, self.LOG):
                if self.up[v][j - 1] != -1:
                    self.up[v][j] = self.up[self.up[v][j - 1]][j - 1]
            self._dfs(v, node)

    def _preprocess(self):
        """Precompute ancestors and distances starting from root."""
        self.up[self.root][0] = -1
        self.depth[self.root] = 0
        self.dist[self.root] = 0
        self._dfs(self.root, -1)

    def lca(self, u, v):
        """
        Compute Lowest Common Ancestor using binary lifting.
        Uses DP table to jump in powers of two:
        - If depth difference is d, lift u by d using binary decomposition.
        - Then lift both nodes together until their ancestors match.
        """
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for j in range(self.LOG):
            if diff & (1 << j):
                u = self.up[u][j]
        if u == v:
            return u
        for j in reversed(range(self.LOG)):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]
        return self.up[u][0]

    def distance(self, u, v):
        """Compute distance between two nodes using LCA and dist[] array."""
        lca = self.lca(u, v)
        return self.dist[u] + self.dist[v] - 2 * self.dist[lca]    

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        N = len(edges) + 1
        # key ideas:
        # 1) we first need to be able to pre-compute the distances (no. of edges)
        # between any pair of nodes using an efficient algorithm (binary lifting + LCA)

        # 2) given the distance between a pair, we can mathematically determine
        # the number of combinations for odd weight sum to be 2^(n-1)

        g = defaultdict(list)
        # build graph
        for u, v in edges:
            g[u].append((v, 1)) # equal weight edges
            g[v].append((u, 1))

        # build tree which preprocesses the graph in O(nLogn) 
        tree = TreeDistance(g, n=N, root=1)

        ans, MOD = [], int(1e9 + 7)
        # each query for distance now runs O(Logn)
        for u, v in queries:
            d = tree.distance(u, v)
            # notice for the assigned edge weights to be odd
            # the number of edges on the path assigned 1 have to be odd
            # i.e. suppose there are d edges in the path between (u, v)
            # we have dC1 + dC3 + dC5 + ... dCk ways to form odd-sum edge weight
            # given that k is the biggest odd number <= d

            # it can be mathematically proven that the sum can
            # be rewritten as 2^(n - 1)
            numWays = 1 << (d-1) if d > 0 else 0
            ans.append(numWays % MOD) 

        return ans

edges, queries = [[1,2]], [[1,1],[1,2]]
edges, queries = [[1,2],[1,3],[3,4],[3,5]], [[1,4],[3,4],[2,5]]

Solution().assignEdgeWeights(edges, queries)