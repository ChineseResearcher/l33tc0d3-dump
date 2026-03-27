# dp - hard
from typing import List
from string import ascii_lowercase as lwc
class UnionFind:
    def __init__(self, size:int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i:int) ->int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i:int, j:int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1

    def connected(self, i:int, j:int) -> bool:
        return self.find(i) == self.find(j)

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:

        n = len(lcp)
        # key ideas:
        # 1) use DSU to construct the potential candidate string
        # 2) solve the Longest Common Suffix dp problem on the candidate string
        # and test if the states match lcp exactly
        dsu = UnionFind(n)
        for i in range(n):
            for j in range(i, n):

                # check for upper bound violation
                if lcp[i][j] > n - max(i, j):
                    return ""

                # check for mirroring violation
                if lcp[i][j] != lcp[j][i]:
                    return ""

                # check for grouping violation
                if lcp[i][j] == 0 and dsu.connected(i, j):
                    return ""

                # otherwise, union the pair iff s[i:] and s[j:] has common prefix
                if lcp[i][j] > 0:
                    dsu.union(i, j)

        # apply greedy letter assignment to each group in DSU
        greedy_id, assigned = 0, dict()
        for i in range(n):
            par = dsu.parent[i]
            if par not in assigned:
                # catch the case where 26 lowercase letters ran out
                if greedy_id > 25:
                    return ""

                assigned[par] = greedy_id
                greedy_id += 1

        candidate = ''.join([lwc[assigned[dsu.parent[i]]] for i in range(n)])

        def longCommSuffix(s1: str, s2:str) -> List[List[int]]: 
            
            n = len(s1)
            # dp[i][j] indicates the longest common suffix that 
            # ends at s1[i] and s2[j]
            dp = [[0] * n for _ in range(n)]

            for i in range(n-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if s1[i] == s2[j]:
                        dp[i][j] = (dp[i + 1][j + 1] if i+1<n and j+1<n else 0) + 1
                    else:
                        dp[i][j] = 0

            return dp

        if longCommSuffix(candidate, candidate) == lcp:
            return candidate

        return ""
    
lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]

Solution().findTheString(lcp)