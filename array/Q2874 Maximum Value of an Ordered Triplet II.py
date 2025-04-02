# array - medium
class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        # this problem tests on pre-building left/right max arr.

        leftmax, rightmax = [float('-inf')] * n, [float('-inf')] * n
        for i in range(1, n):
            leftmax[i] = max(nums[i-1], leftmax[i-1])

        for i in range(n-2, -1, -1):
            rightmax[i] = max(nums[i+1], rightmax[i+1])

        max_diff = [float('-inf')] * n
        # we would rely on the leftmax arr. to build max. nums[i] - nums[j]
        for j in range(1, n-1):
            max_diff[j] = leftmax[j] - nums[j]

        ans = 0
        # search for positive ans. by exploring combination of max_diff & rightmax
        for j in range(1, n-1):
            ans = max(ans, max_diff[j] * rightmax[j])

        return ans
    
nums = [12,6,1,2,7]
nums = [1,10,3,4,19]
nums = [1,2,3]

Solution().maximumTripletValue(nums)