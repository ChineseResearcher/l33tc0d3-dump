# graph - medium
from typing import List
from collections import deque, defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) we are given that city 1 & n are in the same component,
        # thus we just need to BFS from city 1, and record all members
        # belonging to this group
        # 2) for every road, if both ends are in the visited set,
        # we compare its edge dist. against best answer and improve

        g = defaultdict(list)
        for u, v, c in roads:
            g[u].append((v, c))
            g[v].append((u, c))

        visited, q = set([1]), deque([1])
        while q:

            i = q.popleft()
            for j, c in g[i]:
                if j not in visited:
                    q.append(j)
                    visited.add(j)

        ans = float('inf')
        for u, v, c in roads:
            if u in visited and v in visited:
                ans = fmin(ans, c)

        return ans

n, roads = 4, [[1,2,2],[1,3,4],[3,4,7]]
n, roads = 4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]

Solution().minScore(n, roads)