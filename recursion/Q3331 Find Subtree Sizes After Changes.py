# recursion - medium
from typing import List
from collections import defaultdict
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        
        n = len(parent)
        # helper to build graph
        def get_graph(parent):

            g = defaultdict(list)
            for i, j in enumerate(parent):
                g[j].append(i)

            return g

        # helper to find subtree sizes
        def get_subtree_size(graph):

            size = defaultdict(int)
            def dfs(graph, curr):

                if not graph[curr]:
                    size[curr] = 1
                    return 1
                
                # the root itself is considered a member
                curr_res = 1
                for child in graph[curr]:
                    curr_res += dfs(graph, child)

                size[curr] = curr_res
                return curr_res
            
            _ = dfs(graph, 0)
            return size

        g_ori = get_graph(parent)
        near = {char:-1 for char in set(s)} 
        # mark root
        near[s[0]] = 0

        self.change = []
        def backtrack(curr, near):

            for child in g_ori[curr]:

                prev = near[s[child]]
                # detect for potential re-assignment
                # 1) check for if previously seen
                # 2) check for unequal indices
                if prev != -1 and child != prev and parent[child] != prev:
                    self.change.append((child, prev)) # <child, new_parent>

                near[s[child]] = child
                backtrack(child, near)
                # roll back val
                near[s[child]] = prev

        _ = backtrack(0, near)
        # change arr. would record the re-assignments
        # just update parent arr. according to changes
        for c, p in self.change:
            parent[c] = p

        # build a modified graph based on updated parent arr.
        g_mod = get_graph(parent)
        res = get_subtree_size(g_mod)
        return [res[i] for i in range(n)]          
    
parent, s = [-1,0,0,1,1,1], "abaabc"
parent, s = [-1,0,4,0,1], "abbba"

Solution().findSubtreeSizes(parent, s)