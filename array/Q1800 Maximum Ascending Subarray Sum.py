# array - easy
class Solution:
    def maxAscendingSum(self, nums) -> int:
        n = len(nums)

        ans = nums[0]
        # use a variable to track curr. sum of an ascending subarray
        currSum = nums[0]

        for i in range(1, n):

            if nums[i] <= nums[i-1]:
                ans = max(ans, currSum)
                currSum = nums[i]
                continue

            currSum += nums[i]
            if i == n-1: ans = max(ans, currSum)

        return ans
    
nums = [10,20,30,5,10,50]
nums = [10,20,30,40,50]
nums = [12,17,15,13,10,11,12]

Solution().maxAscendingSum(nums)