# graph - medium
from typing import List
from collections import defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:        

        # core ideas:
        # 1) build a bi-directed graph of dislikes
        # 2) build a global grouping dict and detect conflict in group assignment
        # using DFS traversal for unvisited nodes

        g = defaultdict(list)
        for u, v in dislikes:
            g[u].append(v)
            g[v].append(u)

        grouping = {i:-1 for i in range(1, n+1)}

        ans = True
        def dfs(node, assignment):

            nonlocal ans
            # assign
            grouping[node] = assignment
            if not g[node]:
                return
            
            for neighbour in g[node]:

                # indication of clash between assigned grp and to-assign grp
                if grouping[neighbour] != -1:
                    if grouping[neighbour] != 1 - assignment:
                        ans = False
                        return

                    continue
                
                dfs(neighbour, 1-assignment) # alternate assignment 0 / 1

        for node in range(1, n+1):
            # unvisited / unprocessed
            if grouping[node] == -1:
                
                # always default to group 0 for the unvisited
                dfs(node, 0)
                if not ans:
                    return ans

        return ans
    
n, dislikes = 4, [[1,2],[1,3],[2,4]]
n, dislikes = 3, [[1,2],[1,3],[2,3]]

Solution().possibleBipartition(n, dislikes)