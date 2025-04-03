# greedy - medium
class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        # in order for a unsorted subarr. to be part of a bigger
        # sorted arr., there can only be one such subarr.
        leftMax, rightMin = [float('-inf')] * n, [float('inf')] * n

        # fill the values for two auxiliary arrays
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], nums[i-1])

        for i in range(n-2, -1, -1):
            rightMin[i] = min(rightMin[i+1], nums[i+1])

        # the shortest subarr. is implied by the first violation
        # of nums[i] w.r.t. to each of the auxiliary array
        l, r = n, 0

        for i in range(n-1):
            if nums[i] > rightMin[i]:
                l = i
                break

        for i in range(n-1, 0, -1):
            if nums[i] < leftMax[i]:
                r = i
                break

        return r-l+1 if r > l else 0
    
nums = [2,6,4,8,10,9,15]
nums = [1,3,2,4]

Solution().findUnsortedSubarray(nums)