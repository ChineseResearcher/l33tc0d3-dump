# binary search - medium
import bisect
from typing import List
class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:

        n = len(costs)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) first sort the costs
        # 2) for every costs[i], find furthest j using binary search s.t. 
        # costs[i] + costs[j] < budget

        info = [(costs[i], capacity[i]) for i in range(n)]
        info.sort()

        # prefix first / second max on capacity values
        pf_1st_max, pf_2nd_max = [None] * n, [None] * n
        # compute prefix max
        top_2 = [0, 0]
        for i in range(n):
            v = info[i][1]

            if v >= top_2[1]:
                top_2 = [top_2[1], v]
            elif top_2[0] < v < top_2[1]:
                top_2 = [v, top_2[1]]

            # compare w/ existing and update
            if top_2[1] > 0: pf_1st_max[i] = top_2[1]
            if top_2[0] > 0: pf_2nd_max[i] = top_2[0]

        ans = 0
        for i in range(n):
            i_cost, i_cap = info[i]
            if i_cost >= budget:
                continue

            j = bisect.bisect_right(info, budget-i_cost-1, key=lambda t: t[0]) - 1
            # no pair formed, use this machine only
            if j < 0:
                ans = fmax(ans, i_cap)
                continue
            
            if j > i:
                if i_cap != pf_1st_max[j]:
                    capSum = i_cap + pf_1st_max[j]
                else:
                    capSum = pf_1st_max[j] + pf_2nd_max[j]
                ans = fmax(ans, capSum)
            elif j == i:
                ans = fmax(ans, i_cap + (pf_1st_max[j-1] if j - 1 >= 0 else 0))
            elif j < i:
                ans = fmax(ans, i_cap + pf_1st_max[j])

        return ans
    
costs, capacity, budget = [2,2,2], [3,5,4], 5
costs, capacity, budget = [4,8,5,3], [1,5,2,7], 8
costs, capacity, budget = [3,5,7,4], [2,4,3,6], 7

Solution().maxCapacity(costs, capacity, budget)