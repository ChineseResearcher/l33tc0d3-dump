# greedy - medium
class Solution:
    def jump(self, nums):
        n = len(nums)
        # edge case: nums is length 1
        if n == 1: return 0

        # the qn guarantees reachable to the end, so first
        # element in nums is definitely non-zero
        maxJump = nums[0]

        # as maxJump is init. to nums[0], assume we have taken first step
        ans = 1

        if maxJump >= n-1: return ans
        for i in range(n-1):
            for j in range(i+1, maxJump+1):
                maxJump = max(maxJump, j + nums[j])
                if maxJump >= n-1:
                    return ans + 1

            ans += 1

nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
nums = [1,2]

Solution().jump(nums)