# binary search - hard
from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        # build an O(M) checker to validate if can run for k minutes
        def canRun(batteries: List[int], k: int, n: int) -> bool:

            m = len(batteries)
            # given a sorted batteries array, test if we can
            # run n computers for at least k minutes simultaneously

            # the greedy strategy is to distribute the sum of remaining 
            # battery time after subtracting the n largest batteries evenly
            # to all the n largest batteries
            leftover = sum(batteries[:m-n])

            # if there's no leftover to distribute, i.e. n = len(batteries)
            if leftover == 0:
                return (min(batteries) >= k)

            # start the distribution from the smallest of the n largest
            idx = m - n
            runtime, smallerCnt = batteries[idx], 1
            # print(f'trying k = {k} w/ runtime init. to {runtime}')
            while True:

                while idx+1 < m and batteries[idx+1] == batteries[idx]:
                    smallerCnt += 1
                    idx += 1
                
                # batteries arr. already exhausted
                if idx == m-1:
                    runtime += leftover // smallerCnt
                    break

                # or that the leftover battery minutes can't be fully distributed 
                # to the smaller batteries we just scanned in the while-loop
                full_dist = (batteries[idx+1] - batteries[idx]) * smallerCnt

                if leftover < full_dist:
                    runtime += leftover // smallerCnt
                    break

                # otherwise there's a bigger battery to completely match up to
                runtime += (batteries[idx+1] - batteries[idx])
                leftover -= full_dist

                # if have reached the desired runtime of k minutes, early stop
                if runtime >= k:
                    break

                idx += 1
                smallerCnt += 1

            return (runtime >= k)

        # sort the batteries in asc. order first
        batteries.sort()

        # maximally the computers can only run for sum of battery minutes // n
        l, r = 1, sum(batteries) // n

        ans = 0
        while l <= r:

            k = (l + r) // 2
            if canRun(batteries, k, n):
                l = k + 1
                ans = max(ans, k)

            else:
                r = k - 1

        return ans
    
n, batteries = 2, [3,3,3]
n, batteries = 2, [1,1,1,1]
n, batteries = 2, [4,1,4,4]
n, batteries = 3, [10,10,5,3]
n, batteries = 3, [5,7,9,10]
n, batteries = 8, [15,27,40,63,69,71,72,79,87,97]

Solution().maxRunTime(n, batteries)