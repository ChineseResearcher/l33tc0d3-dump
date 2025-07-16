# dp - medium
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        # we can just brute-force all possible formations:

        ans = 0
        # 1) odd-odd
        res1 = len([x for x in nums if x % 2 == 1])
        if res1 > 1:
            ans = max(ans, res1)

        # 2) even-even
        res2 = n - res1
        if res2 > 1:
            ans = max(ans, res2)

        # 3) odd-even OR even-odd
        res3 = [nums[0]]
        for i in range(1, n):
            if res3[-1] % 2 == 0 and nums[i] % 2 == 1:
                res3.append(nums[i])

            if res3[-1] % 2 == 1 and nums[i] % 2 == 0:
                res3.append(nums[i])
        if len(res3) > 1:
            ans = max(ans, len(res3))

        return ans
    
nums = [1,2,3,4]
nums = [1,2,1,1,2,1,2]
nums = [1,3]

Solution().maximumLength(nums)