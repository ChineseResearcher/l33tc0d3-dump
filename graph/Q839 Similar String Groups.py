# graph - hard
from typing import List
from collections import defaultdict, deque
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        strs = list(set(strs))
        n, m = len(strs), len(strs[0])
        # helper to determine if two anagrams only differ by two characters
        def diff_by_two(a: str, b: str) -> bool:
            cnt = 0
            for i in range(m):
                if a[i] != b[i]:
                    cnt += 1
                if cnt > 2:
                    return False
            return cnt == 2

        # build graph
        g = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if diff_by_two(strs[i], strs[j]):
                    g[i].append(j)
                    g[j].append(i)

        # bfs to discover group count
        visited, ans = set(), 0
        for i in range(n):

            if i not in visited:
                # mark new group
                ans += 1

                visited.add(i)
                q = deque([i])
                while q:

                    curr = q.popleft()
                    for neighbour in g[curr]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)

        return ans

strs = ["omv","ovm"]
strs = ["abc","abc"]
strs = ["tars","rats","arts","star"]

Solution().numSimilarGroups(strs)
