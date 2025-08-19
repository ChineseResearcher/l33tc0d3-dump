# dp - medium
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:  

        n = len(nums)
        # core ideas:
        # 1) there are two possible cases for a max-sum subarray:
        # (a) subarray that does not loop over OR (b) subarray that does

        # 2) for case (a), this can be solved by Kadane's, for case (b)
        # which we can represent as [...i___j...], where nums[j:] + nums[:i+1] 
        # is the cross-overed max-sum subarray, we consider nums[i+1:j], and
        # this portion is exactly the opposite, the min-sum subarr, which can
        # again be found using Kadane's algo

        # one special corner case is when all numbers are -ve
        # then if we search for case (b) the min-sum subarr would cover the entire arr
        # making case (b) invalid for comparison
        if max(nums) < 0:
            return max(nums)

        # solve for case (a): max-sum subarr.
        case_a, best_sum = float('-inf'), float('-inf')
        for x in nums:
            best_sum = max(best_sum + x, x)
            case_a = max(case_a, best_sum)

        # solve for case (b): min-sum subarr.
        case_b, best_sum = float('inf'), float('inf')
        for x in nums:
            best_sum = min(best_sum + x, x)
            case_b = min(case_b, best_sum)

        return max(case_a, sum(nums) - case_b)
    
nums = [1,-2,3,-2]
nums = [1,-2,3,10]
nums = [5,-3,5]
nums = [-5,3,5]
nums = [-3,-2,-3]
nums = [6,9,-3]
nums = [-2,-8,6,9,2]

Solution().maxSubarraySumCircular(nums)