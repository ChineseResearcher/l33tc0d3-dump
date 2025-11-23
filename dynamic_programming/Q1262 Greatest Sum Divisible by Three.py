# dp - medium
from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        n = len(nums)
        # key ideas:
        # 1) any possible sum would have modulo states [0,1,2] when divided by 3
        # 2) build our DP arr considering the three states ending at each index
        dp = [-1] * 3
        dp[nums[0] % 3] = nums[0]

        for i in range(1, n):

            new_dp, curr_mod = [-1] * 3, nums[i] % 3
            for mod_state in [0, 1, 2]:

                if mod_state == curr_mod:
                    new_dp[mod_state] = max(dp[0], 0) + nums[i]
                else:
                    prev_mod = (mod_state - curr_mod + 3) % 3
                    # use curr. number 
                    if dp[prev_mod] != -1:
                        new_dp[mod_state] = dp[prev_mod] + nums[i]
                
                # don't use curr. number
                new_dp[mod_state] = max(new_dp[mod_state], dp[mod_state])

            # constant space optimisation
            dp = new_dp
            
        return max(dp[0], 0)

nums = [4]
nums = [3,6,5,1,8]
nums = [1,2,4,3,4]

Solution().maxSumDivThree(nums)