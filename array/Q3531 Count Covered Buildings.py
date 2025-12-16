# array - medium
from typing import List
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        # maintain the leftmost / rightmost, upmost / downmost
        # col and row accordingly for each row and col
        l, r, u, d = dict(), dict(), dict(), dict()

        fmin = lambda a, b: a if a <= b else b
        fmax = lambda a, b: a if a >= b else b

        for x, y in buildings:
            if y not in l:
                l[y] = n + 1
            l[y] = fmin(l[y], x)
            
            if y not in r:
                r[y] = 0
            r[y] = fmax(r[y], x)

            if x not in u:
                u[x] = 0
            u[x] = fmax(u[x], y)

            if x not in d:
                d[x] = n + 1
            d[x] = fmin(d[x], y)

        # second pass to determine covered-ness
        ans = 0
        for x, y in buildings:
            if l[y] < x < r[y] and d[x] < y < u[x]:
                ans += 1

        return ans
    
n, buildings = 3, [[1,2],[2,2],[3,2],[2,1],[2,3]]
n, buildings = 3, [[1,1],[1,2],[2,1],[2,2]]
n, buildings = 5, [[1,3],[3,2],[3,3],[3,5],[5,3]]

Solution().countCoveredBuildings(n, buildings)