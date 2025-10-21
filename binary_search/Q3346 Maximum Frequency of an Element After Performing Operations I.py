# binary search - medium
from typing import List
import bisect
from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        n = len(nums)
        # core ideas:
        # 1) first sort nums, then process every number in range [nums[l]...nums[r]]
        # 2) use binary search to locate the valid span of elements that could be converted
        # to curr. explored number "x" via operation
        # 3) if the explored "x" happens to exist in nums arr., then we take into account its freq.
        c = Counter(nums)
        nums.sort()

        l, r, ans = nums[0], nums[-1], 0
        for x in range(l, r+1):

            valid_cnt = bisect.bisect_right(nums, x + k) - bisect.bisect_left(nums, x - k)
            # "x" being a number in nums arr. should be discounted from valid_cnt
            valid_cnt -= c[x]

            # subject to max. numOperations
            curr_ans = valid_cnt if valid_cnt <= numOperations else numOperations
            curr_ans += c[x]

            if curr_ans > ans:
                ans = curr_ans

        return ans
    
nums, k, numOperations = [1,4,5], 1, 2
nums, k, numOperations = [5,11,20,20], 5, 1
nums, k, numOperations = [88,53], 27, 2
nums, k, numOperations = [23,54], 77, 1
nums, k, numOperations = [58,80,5], 58, 2

Solution().maxFrequency(nums, k, numOperations)