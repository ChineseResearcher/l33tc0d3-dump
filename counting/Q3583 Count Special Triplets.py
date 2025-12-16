# counting - medium
from collections import Counter
from typing import List
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        freq_sf = Counter(nums[1:])
        freq_pf = Counter(nums[:1])

        ans, MOD = 0, int(1e9 + 7)
        for i in range(1, n-1):

            freq_sf[nums[i]] -= 1

            target = nums[i] * 2
            ans += freq_pf[target] * freq_sf[target]
            ans %= MOD

            freq_pf[nums[i]] += 1

        return ans
    
nums = [6,3,6]
nums = [0,0,0,0,0]
nums = [8,4,2,8,4]

Solution().specialTriplets(nums)