# dp - medium
class Solution:
    def maxAbsoluteSum(self, nums):
        n = len(nums)

        # question asks for max. abs sum, we can break the problem into
        # two sub-problems, each asking of max. sum & min.sum

        # construct dp arr. of size n
        # Note: it is impossible to tackle the abs. max problem using only one dp arr.
        dp_max, dp_min = [0] * n, [0] * n

        # initiate the first num in dp
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        # the core idea is Kadane's algorithm, an iterative DP approach
        # although we could also get rid of dp arr. and just keep a greedy max/min var.
        ans = max(abs(dp_max[0]), abs(dp_min[0]))

        # first pass tackle the max. sum problem
        for i in range(1, n):

            dp_max[i] = max(dp_max[i-1] + nums[i], nums[i])
            ans = max(ans, abs(dp_max[i]))

        # second pass tackle the min. sum problem
        for i in range(1, n):

            dp_min[i] = min(dp_min[i-1] + nums[i], nums[i])
            ans = max(ans, abs(dp_min[i]))

        return ans
    
nums = [1,-3,2,3,-4]
nums = [2,-5,1,-4,3,-2]
nums = [-7,-1,0,-2,1,3,8,-2,-6,-1,-10,-6,-6,8,-4,-9,-4,1,4,-9]
nums = [-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8]
nums = [6,5,-4,-3,5,6,-5,-6,9,-8,-7,3,8,-8,6,8,9,10,7,1]
nums = [-9,-5,-10,-4,4,2,2,-3,-10,5,9,10,8,1,6,-4,4,-2,-5,-7]
nums = [-1,2,-7,-9,0,5,-8,9,-4,8,7,-5,-1,9,7,9,6,-10,-3,-1]
nums = [-4,6,1,9,-9,-5,-9,2,3,10,6,-1,-4,4,-1,-5,-2,-10,-8,1]

Solution().maxAbsoluteSum(nums)