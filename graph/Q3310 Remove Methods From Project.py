# graph - medium
from typing import List
from collections import defaultdict, deque
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        # core ideas:
        # 1) build a direct graph w/ invocations
        # 2) use BFS to mark all "suspicious nodes" by starting at node k
        # 3) mark suspicious nodes "excluded" (if any) via BFS starting from unvisited nodes
        g = defaultdict(list)

        for u, v in invocations:
            g[u].append(v)

        q, visited = deque([k]), set([k])
        while q:

            curr = q.popleft()
            for neighbour in g[curr]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)

        # now visited contain all "suspicious nodes"
        sus = visited.copy()

        # continue operating on visited w/ a new set to store excluded
        # define a checker that returns True immediately when any one
        # of the suspicious nodes is being called from remaining nodes
        def depend_check(seen:set) -> bool:
            
            for node in range(n):
                if node not in seen:

                    q = deque([node])
                    seen.add(node)

                    while q:

                        curr = q.popleft()
                        for neighbour in g[curr]:
                            if neighbour in sus:
                                return True

                            if neighbour not in seen:
                                q.append(neighbour)
                                seen.add(neighbour)

            return False

        if depend_check(visited):
            return [i for i in range(n)]
        else:
            return [i for i in range(n) if i not in sus]
        
n, k, invocations = 4, 1, [[1,2],[0,1],[3,2]]
n, k, invocations = 5, 0, [[1,2],[0,2],[0,1],[3,4]]
n, k, invocations = 3, 2, [[1,2],[0,1],[2,0]]
n, k, invocations = 3, 2, [[1,0],[2,0]]

Solution().remainingMethods(n, k, invocations)