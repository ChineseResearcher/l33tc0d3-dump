# prefix sum - medium
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        n = len(nums)
        pfMax, sfMin = [None] * n, [None] * n

        pfMax[0] = nums[0]
        for i in range(1, n):
            pfMax[i] = max(pfMax[i - 1], nums[i])

        sfMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            sfMin[i] = min(sfMin[i + 1], nums[i])

        for i in range(n):
            score = pfMax[i] - sfMin[i]
            if score <= k: return i

        return -1

nums, k = [5,0,1,4], 3

Solution().firstStableIndex(nums, k)