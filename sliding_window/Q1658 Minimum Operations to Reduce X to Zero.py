# sliding window - medium
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) the problem can be inverted as: find the longest subarray
        # s.t. the sum(nums) - sum(subarray) = x exactly
        # 2) use a sliding window to locate the longest valid subarray (lvs)

        S = sum(nums)
        # edge case where whole nums array is removed
        if S == x: return n

        l, windowSum, lvs = 0, 0, -1
        for r in range(n):

            windowSum += nums[r]
            while l < r and S - windowSum < x:
                windowSum -= nums[l]
                l += 1

            if S - windowSum == x:
                lvs = fmax(lvs, r -l + 1)

        return n - lvs if lvs != -1 else -1

nums, x = [1,1,4,2,3], 5
nums, x = [5,6,7,8,9], 4
nums, x = [3,2,20,1,1,3], 10

Solution().minOperations(nums, x)