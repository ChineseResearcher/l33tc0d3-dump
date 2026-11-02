# number theory - medium
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) we are essentially solving the optimisation problem on
        # min|x_i - k| for i in range [0, n - 1] for our chosen k
        # 2) the median will be the optimal solution to this problem
        nums.sort()
        median = nums[n // 2]

        ans = 0
        for x in nums:
            ans += abs(x - median)

        return ans

nums = [1,2,3]
nums = [1,10,2,9]

Solution().minMoves2(nums)