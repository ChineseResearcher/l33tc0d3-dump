# greedy - medium
from typing import List
class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        
        # key ideas:
        # 1) maintain an upper bound array
        # 2) propagate bound restrictions using diff. array in two passes -> left + right

        ub = [float('inf')] * n
        ub[0] = 0

        r = dict()
        for i, b in restrictions:
            r[i] = b

        # track the curr. applicable bound
        curr = -1
        # right pass
        for i in range(1, n):

            curr = ub[i-1] + diff[i-1]
            # an restriction also in-place for curr. index
            if i in r and r[i] < curr:
                curr = r[i]

            ub[i] = min(ub[i], curr)

        curr -1
        # left pass
        for i in range(n-2, -1, -1):

            curr = ub[i+1] + diff[i]
            if i in r and r[i] < curr:
                curr = r[i]

            ub[i] = min(ub[i], curr)

        return max(ub)

n, restrictions, diff = 10, [[3,1],[8,1]], [2,2,3,1,4,5,1,1,2]
n, restrictions, diff = 8, [[3,2]], [3,5,2,4,2,3,1]

Solution().findMaxVal(n, restrictions, diff)