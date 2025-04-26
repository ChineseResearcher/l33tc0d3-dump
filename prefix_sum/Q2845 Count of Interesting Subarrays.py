# prefix sum - medium
from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        
        # this question is an extension/generalisation of LC974
        # where the subarray is divisible by k, or in other words subarrSum % k = 0
        n = len(nums)

        # hashtable is required for efficient counting
        pfSumMod = defaultdict(int)
        # init. pfSum of 0 to 1
        pfSumMod[0] += 1

        # our prefix sum is the running sum of elements
        # s.t nums[i] % modulo == k
        pfSum, ans = 0, 0
        for i in range(n):
            
            pfSum += 1 if nums[i] % modulo == k else 0
            remainder = pfSum % modulo
            # the challenging part is knowing which hashkey to ref
            # in LC974, k is just 0, making remainder itself the ref. key
            ref_remainder = (remainder - k + modulo) % modulo
            ans += pfSumMod[ref_remainder]
            
            # increment the freq. of curr remainder
            pfSumMod[remainder] += 1
        
        return ans
    
nums, modulo, k = [3,2,4], 2, 1
nums, modulo, k = [3,1,9,6], 3, 0

Solution().countInterestingSubarrays(nums, modulo, k)