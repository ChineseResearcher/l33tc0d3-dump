# sliding window - medium
from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) maintain a frequency map of in-the-window distinct numbers
        # 2) shrink window whenever the curr. freq. exceeds k
        freq = defaultdict(int)

        l, ans = 0, 0
        for r in range(n):

            xr = nums[r]
            freq[xr] += 1

            while freq[xr] > k:
                xl = nums[l]
                freq[xl] -= 1
                l += 1

            ans = fmax(ans, r - l + 1)

        return ans

nums, k = [5,5,5,5,5,5,5], 4
nums, k = [1,2,1,2,1,2,1,2], 1
nums, k = [1,2,3,1,2,3,1,2], 2

Solution().maxSubarrayLength(nums, k)