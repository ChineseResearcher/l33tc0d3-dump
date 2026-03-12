# graph - hard
from typing import List
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        # already union-ed (in the same cluster)
        if pa == pb:
            return False

        # union by rank
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1

        _, _ = self.find(a), self.find(b)
        # union-ed two clusters
        return True

    def copy(self):
        c = DSU(len(self.parent))
        c.parent = self.parent[:]
        c.rank = self.rank[:]
        return c

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) use binary search on stability, floor (l) is determined by min of all
        # edge strengths, ceiling (r) is determined by the minimum of the min of must-have
        # edges, and 2 * the max of optional edges 

        # 2) first try to union all must-have edges, if the graph already violates
        # spanning tree, i.e. having cycle(s), early return

        # 3) suppose the M must-have edges do not form cycle(s), we continue building
        # our spanning tree with N-1-M edges from the optional edges list
        mst = DSU(n)

        must_min, opt_min, opt_max = float('inf'), float('inf'), float('-inf')
        optional = []
        for u, v, strength, type in edges:
            if type == 1:
                must_min = fmin(must_min, strength)
                if not mst.union(u, v):
                    return -1
            else:
                opt_min = fmin(opt_min, strength)
                opt_max = fmax(opt_max, strength)
                optional.append((strength, u, v))

        m = len(edges) - len(optional)
        # we still have "p" more edges to pick from optional
        p = n - 1 - m

        # if must-have edges already add up to n-1 edges and do form a spanning tree
        if p == 0:
            return must_min

        # if optional edges < p, early return
        if len(optional) < p:
            return -1

        # sort optional edges by strength descending
        optional.sort(reverse=True)

        # define [l, r] for binary search
        l, r = fmin(must_min, opt_min), fmin(must_min, opt_max * 2)
        def possible(target: int, base_mst: DSU) -> bool:
            
            mst = base_mst.copy()
            # subject to k upgrades, can we find p more edges
            # from optional list s.t. the min. strength >= target
            up, picked, i = 0, 0, 0
            while picked < p and i < len(optional):

                curr = optional[i]
                s, u, v = curr[0], curr[1], curr[2]
                if s >= target:
                    if mst.union(u, v):
                        picked += 1
                else:
                    if up < k and 2 * s >= target:
                        if mst.union(u, v):
                            picked += 1
                            up += 1

                i += 1

            return picked == p
        
        ans = -1
        while l <= r:

            target = (l + r) // 2
            if possible(target, mst):
                ans = fmax(ans, target)
                l = target + 1
            else:
                r = target - 1

        return ans

n, edges, k = 3, [[0,1,2,1],[1,2,3,0]], 1
n, edges, k = 3, [[0,1,4,0],[1,2,3,0],[0,2,1,0]], 2
n, edges, k = 3, [[0,1,1,1],[1,2,1,1],[2,0,1,1]], 0

Solution().maxStability(n, edges, k)