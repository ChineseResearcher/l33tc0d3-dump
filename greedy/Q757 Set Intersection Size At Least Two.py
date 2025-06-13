# greedy - hard
from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # sorting in the correct fashion is the hardest part of this problem
        # as our goal is to re-use our chosen numbers as much as possible
        # for a given interval, we should always choose intvl[-1], and intvl[-1]-1 if possible
        # s.t. we could overlap as much as possible w/ the next interval
        # to facilitate this, we first sort based on RIGHT ends in ASC order
        # by sorting it this way we are always probing for the next must-add bigger number
        intervals.sort(key = lambda x: x[1])

        # as we need to make sure every interval has two representative in the set we choose
        # we keep track of the two largest numbers chosen so far and test against each interval
        a, b = intervals[0][-1],  intervals[0][-1]-1

        n = len(intervals)

        ans = 2
        for i in range(1, n):

            l_end, r_end = intervals[i][0], intervals[i][1]
            if a < l_end:
                a = r_end
                ans += 1

            if b < l_end:
                b = r_end if a != r_end else r_end-1
                ans += 1

            # make sure a is the larger one
            if b > a:
                a, b = b, a

        return ans
    
intervals = [[1,3],[3,7],[8,9]]
intervals = [[1,3],[1,4],[2,5],[3,5]]
intervals = [[1,2],[2,3],[2,4],[4,5]]
intervals = [[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]]

Solution().intersectionSizeTwo(intervals)