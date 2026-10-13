# two pointers - medium
class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:

        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) use a two-pointer approach to find the rightmost greater / equal element
        # 2) we need to pre-compute an auxiliary suffix max. array

        sfMax = [None] * n
        sfMax[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            sfMax[i] = fmax(nums[i], sfMax[i + 1])

        # second pointer j only goes forward
        j = 0

        ans = 0
        for i in range(n):
            if j <= i:
                j = fmin(i + 1, n - 1)

            while j + 1 < n and sfMax[j + 1] >= nums[i]:
                j += 1

            if sfMax[j] >= nums[i]:
                ans = fmax(ans, j - i)

        return ans

nums = [1,0]
nums = [6,0,8,2,1,5]
nums = [9,8,1,0,1,9,4,0,4,1]

Solution().maxWidthRamp(nums)