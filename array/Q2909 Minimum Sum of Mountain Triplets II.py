# array - medium
class Solution:
    def minimumSum(self, nums):
        n = len(nums)
        # we want to locate mountain triplets, meaning for i < j < k
        # nums[i] < nums[j] & nums[k] < nums[j]

        # pre-build left/right min arr.
        leftmin, rightmin = [float('inf')] * n, [float('inf')] * n
        for i in range(1, n):
            leftmin[i] = min(leftmin[i-1], nums[i-1])

        for i in range(n-2, -1, -1):
            rightmin[i] = min(rightmin[i+1], nums[i+1])

        ans = float('inf')
        # explore j indices, and validate if mountain is formed
        for j in range(1, n-1):
            if nums[j] > leftmin[j] and nums[j] > rightmin[j]:
                ans = min(ans, leftmin[j] + nums[j] + rightmin[j])

        return ans if ans < float('inf') else -1
    
nums = [8,6,1,5,3]
nums = [5,4,8,7,10,2]
nums = [6,5,4,3,4,5]
nums = [1,2,3,2]

Solution().minimumSum(nums)