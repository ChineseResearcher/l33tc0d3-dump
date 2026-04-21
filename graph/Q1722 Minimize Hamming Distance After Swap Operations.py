# graph - medium
from typing import List
from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        # key ideas:
        # 1) indices that can be reached via swaps connection form a group
        # 2) any pair(s) of indices in a group can be directly / indirectly swapped
        # 3) track the parent of each indice, and the membership under each parent index
        visited = set()

        g = defaultdict(list)
        for u, v in allowedSwaps:
            g[u].append(v)
            g[v].append(u)

        def dfs(currIdx:int, parentIdx:int) -> None:

            nonlocal visited
            visited.add(currIdx)
            par_info[currIdx] = parentIdx

            grp_info[parentIdx][source[currIdx]] += 1
            for neighbour in g[currIdx]:
                if neighbour not in visited:
                    _ = dfs(neighbour, parentIdx)

        grp_info = dict()
        par_info = dict()

        for i in range(n):
            if i not in visited:

                grp_info[i] = defaultdict(int)
                _ = dfs(i, i)

        # compute hamming distance
        ans = 0
        for i in range(n):

            char = target[i]
            # query for the cnt of target char. in curr. index-group
            if grp_info[par_info[i]][char] == 0:
                ans += 1
                continue

            # if we have free target char. to be exchanged to curr. index
            # we consume one count from its frequency
            grp_info[par_info[i]][char] -= 1

        return ans

source, target, allowedSwaps = [1,2,3,4], [1,3,2,4], []
source, target, allowedSwaps = [1,2,3,4], [2,1,4,5], [[0,1],[2,3]]
source, target, allowedSwaps = [5,1,2,4,3], [1,5,4,2,3], [[0,4],[4,2],[1,3],[1,4]]

Solution().minimumHammingDistance(source, target, allowedSwaps)