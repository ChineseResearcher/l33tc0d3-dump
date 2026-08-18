# array - easy
from typing import List
from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        if k == len(nums): return max(nums)

        freq = Counter(nums)
        if k == 1:
            # largest non-recurring element
            ans = -1
            for x, f in freq.items():
                if f == 1:
                    ans = max(ans, x)
            return ans
        else:
            # only head and tail matters
            a = nums[0] if freq[nums[0]] == 1 else -1
            b = nums[-1] if freq[nums[-1]] == 1 else -1
            return max(a, b)

nums, k = [0,0], 1
nums, k = [0,0], 2
nums, k = [50,0], 1
nums, k = [3,9,2,1,7], 3
nums, k = [3,1,7,10,0], 1
nums, k = [3,9,7,2,1,7], 4

Solution().largestInteger(nums, k)