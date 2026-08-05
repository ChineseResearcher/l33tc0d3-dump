# sliding window - medium
from typing import List
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) we can apply fixed sliding window to solve
        # 2) let the window length be the count of "1"s in nums, and
        # enumerate all possible windows, including the circular ones
        # 3) count of "0"s in every sliding window is the count of swaps needed

        k = nums.count(1)
        # all-zero case & all-one case: no "1"s to be grouped
        if k == 0 or k == n: return 0

        o, z = 0, 0
        for i in range(k):
            if nums[i] == 1:
                o += 1
            else:
                z += 1

        ans = z
        for l in range(1, n):
            r = (l + k - 1) % n
            # adjust in-window counts
            if nums[r] == 1:
                o += 1
            else:
                z += 1

            if nums[l - 1] == 1:
                o -= 1
            else:
                z -= 1

            ans = fmin(ans, z)

        return ans
    
nums = [1,1,0,0]
nums = [1,1,0,0,1]
nums = [0,1,0,1,1,0,0]
nums = [0,1,1,1,0,0,1,1,0]

Solution().minSwaps(nums)