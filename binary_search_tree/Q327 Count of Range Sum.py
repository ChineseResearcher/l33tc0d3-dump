# bst - hard
from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        # we make use of a sortedList to record the prefixSums
        # up to nums[i] if we are iterating up to i
        sl = SortedList([])

        rangeCnt, rSum = 0, 0
        for i in range(n):

            rSum += nums[i]
            # the challenge lies in determining the correct bounds
            # from which we look up the possible existing pfSums
            # s.t. rSum - pfSum falls in the range [lower, upper]
            lb, rb = rSum - upper, rSum - lower
            rangeCnt += sl.bisect_right(rb) - sl.bisect_left(lb)

            # rSum itself also represents the sum of subarr nums[:i+1]
            if lower <= rSum <= upper:
                rangeCnt += 1

            # add curr. running sum to sortedList in the correct pos
            sl.add(rSum)

        return rangeCnt
    
nums, lower, upper = [-2,5,-1], -2, 2
nums, lower, upper = [0], 0, 0

Solution().countRangeSum(nums, lower, upper)