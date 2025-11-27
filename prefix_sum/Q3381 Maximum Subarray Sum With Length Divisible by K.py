# prefix sum - medium
from typing import List
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # key ideas:
        # 1) as per hint, maintain MINIMUM prefix sum ending at every possible i%k
        # 2) this allows us to maximise the subarr. which is guaranteed to be length divisible by k

        fmax = lambda a, b: a if a >= b else b
        fmin = lambda a, b: a if a <= b else b

        # special case: k = 1
        # this turns into Maximum Subarray Sum Problem
        if k == 1:

            ans, rSum = float('-inf'), 0
            for x in nums:
                rSum += x
                rSum = fmax(rSum, x)
                ans = fmax(ans, rSum)

            return ans

        prefix_min, rSum = {i:float('inf') for i in range(k)}, 0
        ans = float('-inf')
        for i in range(n):

            rSum += nums[i]

            j = i % k
            # special case: whenever we reach multiple of k
            if j == k-1:
                ans = fmax(ans, rSum)
            
            # find the relevant subarray with length divisible by k
            prev_min = prefix_min[j]
            range_sum = rSum - prev_min
            ans = fmax(ans, range_sum)
            
            # update prefix_min too considering nums[i]
            prefix_min[j] = fmin(prefix_min[j], rSum)

        return ans

nums, k = [1,2], 1
nums, k = [-1,-2,-3,-4,-5], 4
nums, k = [-5,1,2,-3,4], 2
nums, k = [-7,-9], 1
nums, k = [-35,42,24,49], 2

Solution().maxSubarraySum(nums, k)