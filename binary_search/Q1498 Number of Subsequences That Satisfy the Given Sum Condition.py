# binary search - medium
from typing import List
import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        # it is important to sort nums in asc. order first
        # this allows us to fix nums[i] as the max. val while exploring 
        # possible nums[j] as the min. val in the subseq. for j <= i
        nums.sort()

        ans, MOD = 0, int(1e9 + 7)
        for i in range(n):

            # case 1: nums[i] * 2 <= k
            # cnt = (2^0 + 2^1 + ... + 2^(i-1)) + 1
            # add 1 because [nums[i]] itself is also a valid subseq.
            # the above cnt can be simplified to 2^i using sum of geometric series
            if nums[i] * 2 <= target:
                ans += pow(2, i, MOD)

            # case 2: 
            # we explore all possible nums[j] s.t. if nums[j] is used as the min. val
            # then nums[j] + nums[i] <= target
            # in this case, cnt = (2^k + 2^(k+1) + ... + 2^(i-1))
            # where k is the number of elements in between the rightmost valid nums[j] and nums[i]
            else:

                k = i - bisect.bisect_right(nums, target - nums[i])
                ans += pow(2, i, MOD) - pow(2, k, MOD) # again simplified using sum of GM series

        return ans % MOD
    
nums, target = [3,5,6,7], 9
nums, target = [3,3,6,8], 10
nums, target = [2,3,3,4,6,7], 12

Solution().numSubseq(nums, target)