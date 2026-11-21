# recursion - medium
from collections import defaultdict
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        
        n = len(parent)
        # helper to build graph: <child, parent>
        def get_graph(parent: list[int]) -> defaultdict:
            g = defaultdict(list)
            for i, j in enumerate(parent):
                g[j].append(i)
            return g

        # helper to find subtree sizes
        def get_subtree_size(graph: defaultdict) -> list[int]:
            size = [0] * n
            def dfs(graph, curr):
                if not graph[curr]:
                    size[curr] = 1
                    return 1
                curr_res = 1
                for child in graph[curr]:
                    curr_res += dfs(graph, child)
                size[curr] = curr_res
                return curr_res
            _ = dfs(graph, 0)
            return size

        g = get_graph(parent)
        self.change = []
        def backtrack(curr: int, near: dict) -> None:
            for child in g[curr]:
                prev = near[s[child]]
                # detect for potential re-assignment
                # 1) check for if previously seen
                # 2) check for unequal indices
                if prev != -1 and child != prev and parent[child] != prev:
                    self.change.append((child, prev)) # <child, new_parent>

                near[s[child]] = child
                backtrack(child, near)
                # backtrack
                near[s[child]] = prev

        near = {char: -1 for char in set(s)} 
        near[s[0]] = 0 # mark root
        _ = backtrack(0, near)

        # re-assign parents according to "change"
        for c, p in self.change:
            parent[c] = p

        # count size(s) of subtree(s) after modifications
        return get_subtree_size(get_graph(parent))        
    
parent, s = [-1,0,4,0,1], "abbba"
parent, s = [-1,0,0,1,1,1], "abaabc"

Solution().findSubtreeSizes(parent, s)