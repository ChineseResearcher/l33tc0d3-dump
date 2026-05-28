# greedy - medium
from typing import List
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        # key ideas:
        # 1) there are only 3 possible ways we can form 4-person contiguous group
        # 2) for each row, check if [2,3,4,5], [4,5,6,7], [6,7,8,9] are free
        # 3) n is large (n <= 1e9), we need to optimize by only processing the
        # array storing reserved seats

        taken = defaultdict(list)
        for r, c in reservedSeats:
            taken[r].append(c)

        # for rows where there's no reserved seats at all
        # we can surely place two groups of size-4 reservation
        ans = (n - len(taken)) * 2

        g1 = set([2,3,4,5])
        g2 = set([4,5,6,7])
        g3 = set([6,7,8,9])
        for r in taken.keys():

            b1, b2, b3 = False, False, False
            for c in taken[r]:
                if c in g1:
                    b1 = True
                if c in g2:
                    b2 = True
                if c in g3:
                    b3 = True

            if not b1 and not b3:
                ans += 2
            else:
                if not b1 or not b2 or not b3:
                    ans += 1

        return ans
    
n, reservedSeats = 2, [[2,1],[1,8],[2,6]]
n, reservedSeats = 4, [[4,3],[1,4],[4,6],[1,7]]
n, reservedSeats = 3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]

Solution().maxNumberOfFamilies(n, reservedSeats)