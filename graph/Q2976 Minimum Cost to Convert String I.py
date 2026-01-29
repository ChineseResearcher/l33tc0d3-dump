# graph - medium
from typing import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        n, m = len(source), len(original)
        fmin = lambda a, b: a if a < b else b
        ind = lambda c: ord(c) - ord('a')
        # key ideas:
        # 1) use floyd-warshall to build the optimal dist from each original
        # character to each changed character in O(V^3) time where V <= 26

        # 2) one linear pass from start to end of the source string, and return
        # -1 early to indicate if it's impossible to change some character

        dist = [ [float('inf')] * 26 for _ in range(26) ]
        for i in range(m):
            u, v, w = ind(original[i]), ind(changed[i]), cost[i]
            dist[u][v] = fmin(dist[u][v], w)

        for k in range(26):
            for i in range(26):
                for j in range(26):

                    new_cost = dist[i][k] + dist[k][j]
                    if new_cost < dist[i][j]:
                        dist[i][j] = new_cost

        ans = 0
        for i in range(n):
            # no change needed
            if source[i] == target[i]:
                continue
            # impossible to transform
            if dist[ind(source[i])][ind(target[i])] == float('inf'):
                ans = -1
                break
            # otherwise increment cost w/ optimal dist[i][j]
            ans += dist[ind(source[i])][ind(target[i])]

        return ans
    
source, target = "abcd", "acbe" 
original, changed, cost = ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]

source, target = "aaaa", "bbbb"
original, changed, cost = ["a","c"], ["c","b"], [1,2]

source, target = "abcd", "abce"
original, changed, cost = ["a"], ["e"], [10000]

Solution().minimumCost(source, target, original, changed, cost)