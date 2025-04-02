# array - medium
class Solution:
    def sumOfBeauties(self, nums):
        n = len(nums)
        # as we are targeting a slope formation: nums[j] < nums[i] < nums[k]
        # we need information on the leftmax and rightmin to ensure slope is valid
        leftmax, rightmin = [float('-inf')] * n, [float('inf')] * n

        # pre-build
        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], nums[i-1])
        for i in range(n-2, -1, -1):
            rightmin[i] = min(rightmin[i+1], nums[i+1])

        ans = 0
        # explore all diff. i indices
        for i in range(1, n-1):

            if nums[i] > leftmax[i] and nums[i] < rightmin[i]:
                ans += 2
            elif nums[i] > nums[i-1] and nums[i] < nums[i+1]:
                ans += 1

        return ans
    
nums = [1,2,3]
nums = [2,4,6,4]

Solution().sumOfBeauties(nums)