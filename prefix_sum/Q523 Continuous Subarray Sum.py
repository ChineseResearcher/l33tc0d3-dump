# prefix sum - medium
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        # key ideas:
        # 1) hashmap + prefix sum to locate the previous index
        # where the curr. prefix sum % k is equivalent
        # 2) we want to make sure we only record the earliest index where
        # the modular result is identified

        prefix, pf_sum = {0:-1}, 0
        for i in range(n):
            pf_sum += nums[i]

            pf_sum_mod = pf_sum % k
            if pf_sum_mod in prefix:
                if i - prefix[pf_sum_mod] >= 2:
                    return True
            else:
                prefix[pf_sum_mod] = i

        return False
    
nums, k = [23,2,3,6,7], 6
nums, k = [23,2,6,4,7], 6
nums, k = [23,2,6,4,7], 13

Solution().checkSubarraySum(nums, k)