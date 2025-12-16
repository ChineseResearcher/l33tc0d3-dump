# dp - hard
from functools import cache
from collections import defaultdict
from typing import List
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        
        # build hierarachy (directed) tree
        g = defaultdict(list)
        for u, v in hierarchy:
            # u is the boss of v
            g[u].append(v)

        fmax = lambda a, b: a if a >= b else b

        @cache
        def f(root: int) -> List[List[int]]:

            '''
            f_u[budget][1/0] stands for the max. profit obtained for subtree rooted
            at node "u" with max. budget "budget", with parent of "u" invested (1) or not invested (0)

            similarly, for f_v[budget][1/0]...with parent of "v" (i.e. "u") invested or not invested

            nxt[budget][1/0] stands for the max. profit obtained amongst child nodes of 
            subtree rooted at node "u" (curr. node), with max. budget "budget" and invest status 0/1
            '''

            # 2 x (budget + 1) 2-D dp for curr. node "root"
            f_u = [ [0] * 2 for _ in range(budget + 1) ]

            # 2 x (budget + 1) 2-D dp for curr. node's children
            nxt = [ [0] * 2 for _ in range(budget + 1) ]

            # first populate "nxt" DP array using "f_v"
            for v in g[root]:

                f_v = f(v)

                # note: the iteration direction of budget matters:
                # if we do [0...budget] we would have overcounting

                for i in range(budget,-1,-1): # budget allowed for all child nodes of "u"
                    for j in range(i+1):      # budget allowed for node "v"
                        for k in [0,1]:       # investment decision of node "u"

                            nxt[i][k] = fmax(nxt[i][k], # skip child node "v"
                                             nxt[i-j][k] + f_v[j][k])
                    
            # then populate "f_u" DP array using "nxt"
            for i in range(budget+1):   # budget allowed for subtree rooted at "u"
                for k in [0,1]:         # investment decision of PARENT node of "u"

                    cost = present[root-1] if k == 0 else present[root-1] // 2
                    profit = future[root-1] - cost

                    if i >= cost:
                        f_u[i][k] = fmax(nxt[i][0], # skip node "u"
                                         nxt[i-cost][1] + profit)

                    # allocated budget not enough to invest for "u" 
                    else:
                        f_u[i][k] = nxt[i][0]

            return f_u
                    
        return f(1)[budget][0]

n, present, future, hierarchy, budget = 2, [1,2], [4,3], [[1,2]], 3
n, present, future, hierarchy, budget = 2, [3,4], [5,8], [[1,2]], 4
n, present, future, hierarchy, budget = 3, [4,6,8], [7,9,11], [[1,2],[1,3]], 10
n, present, future, hierarchy, budget = 3, [5,2,3], [8,5,6], [[1,2],[2,3]], 7

Solution().maxProfit(n, present, future, hierarchy, budget)