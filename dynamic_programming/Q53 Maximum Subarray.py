# dp - medium
class Solution:
    def maxSubArray(self, nums):
        
        n = len(nums)
        # kadane's algorithm is a form of DP
        # dp[i] stores the best solution if we consider up to nums[i]
        dp = [0] * n

        dp[0] = nums[0]
        for i in range(1, n):

            # op1: take best solution from dp[i-1] + curr. num
            op1 = dp[i-1] + nums[i]

            # op2: use curr. num only
            op2 = nums[i]

            # choose better option
            dp[i] = max(op1, op2)

        return max(dp)
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
nums = [-1,-2,-3]

Solution().maxSubArray(nums)