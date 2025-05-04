# binary search - hard
from typing import List
import heapq
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        n = len(chargeTimes)

        # build a prefix sum for quick computing of runningCosts in a window
        pf_sum, running_sum = [], 0
        for i in range(n):

            running_sum += runningCosts[i]
            pf_sum.append(running_sum)

        def canRun(k):

            # test if a consecutive window of k robots can be run within budget
            # to validate if the max(chargeTimes) if within the window, we use
            # a maxHeap to lazy-delete the out-of-window elements
            maxHeap = [[-chargeTimes[i], i] for i in range(k)]
            heapq.heapify(maxHeap)

            # if the init. window already falls within budget, early stop
            if -maxHeap[0][0] + k * pf_sum[k-1] <= budget:
                return True
            
            for r in range(k, n):

                heapq.heappush(maxHeap, [-chargeTimes[r], r])
                # lazy-delete
                while maxHeap and maxHeap[0][1] <= r-k:
                    heapq.heappop(maxHeap) 

                # test against the total cost formula
                if -maxHeap[0][0] + k * (pf_sum[r] - pf_sum[r-k]) <= budget:
                    return True
                
            return False

        # max. consecutive is just the count of all robots
        l, r = 1, n

        ans = 0
        while l <= r:

            k = (l + r) // 2
            if canRun(k):
                ans = max(ans, k)
                l = k + 1

            else:
                r = k - 1

        return ans
    
chargeTimes, runningCosts, budget = [3,6,1,3,4], [2,1,3,4,5], 25
chargeTimes, runningCosts, budget = [11,12,19], [10,8,7], 19

Solution().maximumRobots(chargeTimes, runningCosts, budget)