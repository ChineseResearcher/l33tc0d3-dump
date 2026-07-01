# greedy - medium
from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        # key ideas:
        # 1) pre-compute the number of neighbours each node has
        # 2) perform sorting on the computed array, and construct
        # max. total importance by assigning values from high to low
        cnt = [0] * n

        for u, v in roads:
            cnt[u] += 1
            cnt[v] += 1

        cnt.sort(reverse=True)

        ans = 0
        for i in range(n):
            ans += cnt[i] * (n-i)

        return ans

n, roads = 5, [[0,3],[2,4],[1,3]]
n, roads = 5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

Solution().maximumImportance(n, roads)