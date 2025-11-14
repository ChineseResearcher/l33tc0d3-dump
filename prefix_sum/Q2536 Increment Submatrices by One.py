# prefix sum - medium
from typing import List
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        # 2-D differencing arr technique
        diff = [ [0] * n for _ in range(n) ]
        for r1, c1, r2, c2 in queries:

            diff[r1][c1] += 1
            if c2 + 1 < n:
                diff[r1][c2+1] -= 1
            if r2 + 1 < n:
                diff[r2+1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                diff[r2+1][c2+1] += 1

        # override diff with actual sum in two iterations
        # one for col-wise and another for row-wise (order does not matter)

        # col-wise fill
        for r in range(n):
            rSum = 0
            for c in range(n):
                rSum += diff[r][c]
                diff[r][c] = rSum

        # row-wise fill
        for c in range(n):
            rSum = 0
            for r in range(n):
                rSum += diff[r][c]
                diff[r][c] = rSum

        return diff

n, queries = 3, [[1,1,2,2],[0,0,1,1]]
n, queries = 2, [[0,0,1,1]]

Solution().rangeAddQueries(n, queries)