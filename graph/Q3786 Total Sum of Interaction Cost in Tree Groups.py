# graph - hard
from collections import defaultdict, Counter
from typing import List
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        
        # key ideas:
        # 1) if we set all nodes to be the same group, then problem
        # becomes "sum of distances in a tree" which could be solved by
        # looking at how much an edge contributes to the total distance

        # 2) with groupings assigned differently, an edge that links to
        # a subtree with count of grouping "i" = k would contribute 
        # k * (i_total - k) to the interaction costs, where i_total is the
        # frequency count of members assigned "i" in the whole tree

        grp_freq = Counter(group)

        # build graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # global variable
        ans = 0

        # dfs-traversal
        def f(curr:int, parent:int) -> defaultdict:

            nonlocal ans
            curr_cnt = defaultdict(int)
            curr_cnt[group[curr]] += 1

            for neighbour in g[curr]:

                if neighbour == parent:
                    continue

                subtree_cnt = f(neighbour, curr)
                for i, k in subtree_cnt.items():

                    ans += k * (grp_freq[i] - k)
                    curr_cnt[i] += k

            return curr_cnt

        # assume rooted at 0
        _ = f(0, -1)

        return ans

n, edges, group = 3, [[0,1],[1,2]], [1,1,1]
n, edges, group = 3, [[0,1],[1,2]], [3,2,3]
n, edges, group = 4, [[0,1],[0,2],[0,3]], [1,1,4,4]
n, edges, group = 2, [[0,1]], [9,8]

Solution().interactionCosts(n, edges, group)