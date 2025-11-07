# binary search - hard
from typing import List
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:

        n = len(stations)
        # key ideas:
        # 1) binary search on the answer
        # 2) preprocessing using diff. arr. and precompute the power of i-th city 
        # before any extra station installed using prefix sum

        diff = [0] * n
        for i in range(n):
            # decrement happens at index i+r+1
            lb, rb = i - r, i + r + 1
            diff[max(lb, 0)] += stations[i]
            if rb < n:
                diff[rb] -= stations[i]

        power, cSum = [], 0
        for x in diff:
            cSum += x
            power.append(cSum)

        # define the search range for binary search on answer
        L, R = min(power), max(power) + k

        # define O(n) check helper
        # where target is the desired maximin power of a city
        def isPossible(target: int) -> bool:

            # track remaining additional stations
            addSt = k

            # construct diff arr. for extra installations
            extra_diff, extra = [0] * n, 0

            for i in range(n):

                extra += extra_diff[i]
                curr = power[i] + extra

                # no need installation
                if curr >= target:
                    continue

                # otherwise we determine the shortage of stations 
                # and install the additional stations at the ideal locations
                shortage = target - curr
                if addSt < shortage:
                    return False
                
                addSt -= shortage
                extra += shortage
                location = min(i + r, n - 1)

                # mark decrement if relevant
                if location + r + 1 < n:
                    extra_diff[location+r+1] -= shortage

            return True

        ans = L
        while L <= R:

            target = (L + R) // 2
            if isPossible(target):
                if target > ans:
                    ans = target
                L = target + 1
            else:
                R = target - 1

        return ans
    
stations, r, k = [1,1,1,1,1], 2, 1
stations, r, k = [1,1,1,1,1], 2, 0
stations, r, k = [1,2,4,5,0], 1, 2
stations, r, k = [4,4,4,4], 0, 3

Solution().maxPower(stations, r, k)