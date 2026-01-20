# graph - hard
from collections import defaultdict
from typing import List
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        g = defaultdict(list)
        for u, v in enumerate(parent):
            g[u].append(v)
            g[v].append(u)

        g[0].remove(-1)
        del g[-1]

        ans = 0 

        def f(curr:int, par:int) -> int:

            nonlocal ans
            # curr node itself. represents length-1 path
            res = 1

            # use a stack to store all child results
            st = []
            for neighbour in g[curr]:
                if neighbour == par:
                    continue

                n_res = f(neighbour, curr)
                # no path inheritance if char. are the same
                if s[curr] == s[neighbour]:
                    st.append(0)
                    continue

                st.append(n_res)

            st.sort()
            # op1: assume the best path is rooted at curr. node
            # then we build longest length from two best children 
            ans = max(ans, res + sum(st[-2:]))
            # op2: assume the best path passes through curr. node
            # then we build longest length from the best child
            res += sum(st[-1:])

            return res

        _ = f(0, -1)
        return ans
    
parent, s = [-1,0,0,1,1,2], "abacbe"
parent, s = [-1,0,0,0], "aabc"
parent, s = [-1,0,1], "aab"

Solution().longestPath(parent, s)