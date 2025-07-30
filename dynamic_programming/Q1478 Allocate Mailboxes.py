# dp - hard
from typing import List
from functools import cache
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:

        n = len(houses)
        # core ideas:
        # 1) first sort the houses so we have houses lined up from left to right
        # 2) with ordered houses we can define sub-problems as (l, r, k)
        # 3) given some sub-problem (l, r, k), we can split into smaller problems
        # (l, i, 1) and (i+1, r, k-1)
        houses.sort()

        @cache
        def recursive_build(l, r, mb):
            
            if mb == 1:
                # consider the number of houses involved
                med = (l + r) // 2
                if r-l+1 % 2 == 0:
                    # even house count, place the mailbox at the middle
                    # of the two median house positions
                    mbp = (houses[med] + houses[med+1]) // 2
                else:
                    mbp = houses[med]
                # a key result in optimisation is that the median point
                # minimises the total distances to all points on the measured line
                return sum([abs(mbp - houses[i]) for i in range(l, r+1 if r < n else r)])
            
            curr_res = float('inf')
            for i in range(l, r+1 if r < n else r):
                # invalid split
                if (n-1) - (i+1) + 1 < mb-1:
                    break

                res_left = recursive_build(l, i, 1)
                res_right = recursive_build(i+1, r, mb-1)
                curr_res = min(curr_res, res_left + res_right)

            return curr_res
                
        return recursive_build(0, n, k)
    
houses, k = [1,4,8,10,20], 3
houses, k = [2,3,5,12,18], 2

Solution().minDistance(houses, k)