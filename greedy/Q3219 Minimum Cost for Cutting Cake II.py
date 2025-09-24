# greedy - hard
from typing import List
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        
        horizontalCut.sort()
        verticalCut.sort()
        # define two variables that track the number of
        # paper blocks that we would have to cut through if cut hozirontally / vertically
        h_coeff, v_coeff = 1, 1

        ans = 0
        while horizontalCut and verticalCut:

            # compare two cases:
            # 1) cut horizontal -> increment v_coeff -> compare cost for next v cut
            h_cut_cost = h_coeff * horizontalCut[-1] + (v_coeff + 1) * verticalCut[-1] 

            # 2) cut vertical -> increment h_coeff -> compare cost for next h cut
            v_cut_cost = v_coeff * verticalCut[-1] + (h_coeff + 1) * horizontalCut[-1]

            if h_cut_cost > v_cut_cost:
                ans += v_coeff * verticalCut.pop()
                h_coeff += 1

            else:
                ans += h_coeff * horizontalCut.pop()
                v_coeff += 1

        while horizontalCut:
            ans += h_coeff * horizontalCut.pop()

        while verticalCut:
            ans += v_coeff * verticalCut.pop()

        return ans
    
m, n, horizontalCut, verticalCut = 3, 2, [1,3], [5]
m, n, horizontalCut, verticalCut = 2, 2, [7], [4]
m, n, horizontalCut, verticalCut = 6, 3, [2,3,2,3,1], [1,2]
# constraint
import random
m, n, horizontalCut, verticalCut = 100000, 100000, [random.randint(1, 1000) for _ in range(int(1e5))], [random.randint(1, 1000) for _ in range(int(1e5))]

Solution().minimumCost(m, n, horizontalCut, verticalCut)