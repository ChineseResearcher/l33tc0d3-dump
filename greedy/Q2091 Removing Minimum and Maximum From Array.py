# greedy - medium
from typing import List
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) there can only be three ways to remove:
        # - remove both from left
        # - remove both from right
        # - remove the earlier element from left and later element from right
        # 2) take min. of all 3 options

        maxx, minn = max(nums), min(nums)
        i = nums.index(maxx)
        j = nums.index(minn)

        # swap to ensure i < j
        if i > j: i, j = j, i

        op1 = j + 1
        op2 = n - i
        op3 = i + 1 + n - j
        return min(op1, min(op2, op3))

nums = [101]
nums = [2,10,7,5,4,1,8,6]
nums = [0,-4,19,1,8,-2,-3,5]

Solution().minimumDeletions(nums)