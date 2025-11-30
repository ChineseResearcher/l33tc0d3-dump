# prefix sum - medium
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        n = len(nums)
        # key ideas:
        # 1) prefix sum + hashmap (which stores prefix sum % p as key, and latest index as val)
        # 2) obtain a suffix sum too to compute the prefix sum key required

        # first build suffix sum
        sf_sum, rSum = [], 0
        for i in range(n-1, -1, -1):
            rSum += nums[i]
            sf_sum.append(rSum)

        sf_sum = sf_sum[::-1]

        # special case: whole arr. sum is already divisible by p
        if sf_sum[0] % p == 0:
            return 0

        # then iterate forward and update prefix sum hashmap
        pf_hash, ans = {0: -1}, n

        rSum = 0
        for i in range(n):

            rSum += nums[i]
            # update curr. pfSum in pf_hash
            pf_hash[rSum % p] = i

            sfSum = sf_sum[i+1] if i+1 < n else 0
            # obtain ideal prefix hashkey
            pf_key = (p - (sfSum % p)) % p

            # removal of subarr [pf_hash[pf_key]...i] is only valid is such pf_key exists
            if pf_key in pf_hash:

                length = i - pf_hash[pf_key]
                if length < ans:
                    ans = length

        return ans if ans < n else -1

nums, p = [3,1,4,2], 6
nums, p = [6,3,5,2], 9
nums, p = [1,2,3], 3
nums, p = [1,2,3], 5

Solution().minSubarray(nums, p)