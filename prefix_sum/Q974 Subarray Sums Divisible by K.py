# prefix sum - medium
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        # key ideas:
        # 1) prefix sum + hashmap to store count of prefix sum modulo by k
        # 2) when a repeated prefix sum mod k is identified, increment by its stored count
        prefix, pf_sum = {0: 1}, 0

        ans = 0
        for x in nums:
            pf_sum += x
            pf_sum_mod_k = pf_sum % k
            # identify existing count
            if pf_sum_mod_k in prefix:
                ans += prefix[pf_sum_mod_k]
                prefix[pf_sum_mod_k] += 1
            else:
                prefix[pf_sum_mod_k] = 1

        return ans
    
nums, k = [5], 9
nums, k = [4,5,0,-2,-3,1], 5

Solution().subarraysDivByK(nums, k)