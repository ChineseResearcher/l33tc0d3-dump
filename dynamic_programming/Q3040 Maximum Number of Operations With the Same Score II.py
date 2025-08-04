# dp - medium
from typing import List
from functools import cache
class Solution:
    def maxOperations(self, nums: List[int]) -> int: 

        n = len(nums)
        # core ideas:
        # 1) define sub-problems as (l, r) where it indicates we are dealing
        # w/ nums[l...r+1]
        # 2) do it for three possible starting ops
        # 3) turns out a sick optimisation trick was to terminate once we've reached
        # one solution as we are guaranteed that the first dfs that reached l >= r would yield
        # the best solution -> maintain a global variable to terminate early

        @cache
        def recursive_op(l, r, target):

            nonlocal earlyStop
            if earlyStop:
                return 0

            if l >= r:
                earlyStop = True
                return 0
            
            curr_res = 0
            # remove first two
            op1 = nums[l] + nums[l+1]
            if target < 0 or op1 == target:
                curr_res = max(curr_res, 1 + recursive_op(l+2, r, op1))

            # remove last two
            op2 = nums[r] + nums[r-1]
            if target < 0 or op2 == target:
                curr_res = max(curr_res, 1 + recursive_op(l, r-2, op2))

            # remove first and last
            op3 = nums[l] + nums[r]
            if target < 0 or op3 == target:
                curr_res = max(curr_res, 1 + recursive_op(l+1, r-1, op3))

            return curr_res

        earlyStop = False
        return recursive_op(0, n-1, -1)
    
nums = [3,2,1,2,3,4]
nums = [3,2,6,1,4]

Solution().maxOperations(nums)