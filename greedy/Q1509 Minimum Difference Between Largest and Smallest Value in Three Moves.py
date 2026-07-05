# greedy - medium
from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 4: return 0

        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) sorting + greedily pick three elements to change
        # 2) on the sorted array, inspect all possible pairs of
        # (i, j) where j = i + (n-3) - 1, as if we are managing a slided window
        # 3) record the min. possible diff. arising from arr[j] - arr[i]
        nums.sort()

        ans, k = float('inf'), n - 3
        for i in range(4):
            j = i + k - 1
            diff = nums[j] - nums[i]
            ans = fmin(ans, diff)

        return ans

nums = [5,3,2,4]
nums = [3,100,20]
nums = [1,5,0,10,14]
nums = [75,19,78,9,70,5,63,90]

Solution().minDifference(nums)