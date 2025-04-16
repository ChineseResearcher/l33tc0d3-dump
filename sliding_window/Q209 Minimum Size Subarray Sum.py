# sliding window - medium
class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        # handle special case
        # case 1: nums of size 1
        if n == 1:
            return n if nums[0] >= target else 0

        # case 2: first num already satisfies target
        if nums[0] >= target:
            return 1
            
        l = 0 
        subArrSum = nums[0]
        
        minSubArrLength = float('inf')
        
        for r in range(1, n):
            subArrSum += nums[r]
        
            if subArrSum >= target:
                while subArrSum >= target:
                    minSubArrLength = min(minSubArrLength, r-l+1)
                    subArrSum -= nums[l]
                    l += 1

        return 0 if minSubArrLength == float('inf') else minSubArrLength
    
target, nums = 7, [2,3,1,2,4,3]
target, nums = 4, [1,4,4]
target, nums = 11, [1,1,1,1,1,1,1,1]
target, nums = 6, [10,2,3]

Solution().minSubArrayLen(target, nums)