# dp - medium
from typing import List
from functools import cache
import bisect
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        m = len(rides)
        rides.sort()
        startPos = [x[0] for x in rides]

        @cache
        def recursive_ride(idx):

            if idx == m:
                return 0
            
            # op1: skip this ride
            curr_res = recursive_ride(idx+1)

            # op2: use binary search to find the next admissible ride
            # note: we can drop-off and pick-up at the same point
            earning = rides[idx][1] - rides[idx][0] + rides[idx][2]

            j = bisect.bisect_left(startPos, rides[idx][1])
            if j < m and startPos[j] >= rides[idx][1]:
                curr_res = max(curr_res, earning + recursive_ride(j))
            elif j == m:
                curr_res = max(curr_res, earning)

            return curr_res

        return recursive_ride(0)
    
n, rides = 5, [[2,5,4],[1,5,1]]
n, rides = 20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]

Solution().maxTaxiEarnings(n, rides)