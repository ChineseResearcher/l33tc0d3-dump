# dp - hard
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # it is intuitive enough that subproblems should consider some lefr & right bounds
        # but the hard part of this problem is to frame the subproblems as EXCLUSIVE (l,r) bounds
        # and with that a small trick to pad [1] to start/end of nums arr is required
        nums = [1] + nums + [1]

        n = len(nums)
        dp = dict()

        def recursive_burst(l, r):

            if l + 1 == r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            curr_ans = 0
            # similar to partition DP problems like strange printer / remove boxes
            # our dfs explores the possible split k, and here in the range (l, r)
            # the interpretation of this k is equivalent to:
            # what is the last optimal balloon k to burst?
            for k in range(l+1, r):

                left = recursive_burst(l, k)
                right = recursive_burst(k, r)

                # imagine nums[k] burst to last w/ all other balloons in [l+1, ..., r-1] already burst
                curr_ans = max(curr_ans, left + right + \
                                        nums[l] * nums[k] * nums[r]) 
                
            dp[(l, r)] = curr_ans
            return curr_ans

        return recursive_burst(0, n-1)
    
nums = [3,1,5,8]
nums = [1,5]
nums = [1] * 300 # constraint

Solution().maxCoins(nums)