# two pointers - medium
class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):

        n = len(nums)
        # the formula to calculate number of subarr. = n*(n+1) // 2
        ans = 0

        # use a two-pointer approach to track the last idx at which it exceeds right
        prevOver = -1
        for i in range(n):
            
            if nums[i] > right:
                l = i - prevOver - 1
                ans += l * (l + 1) // 2
                prevOver = i
                
            if  (i == n-1 and nums[i] <= right):
                l = i - prevOver
                ans += l * (l+1) // 2
                
        # run through nums again to discount cases due to numbers falling below left
        prevSmaller = None
        for i in range(n):
            
            # we maintain index prevSmaller s.t. it is the left end
            # of a contiguous block of numbers < left
            if prevSmaller is None and nums[i] < left:
                prevSmaller = i
            
            if prevSmaller is not None and nums[i] >= left:
                l = i - prevSmaller
                ans -= l * (l+1) // 2
                prevSmaller = None
                
            # collect last
            if i == n-1 and prevSmaller is not None and nums[i] < left:
                l = i - prevSmaller + 1
                ans -= l * (l+1) // 2

        return ans
    
nums, left, right = [2,1,4,3], 2, 3
nums, left, right = [2,9,2,5,6], 2, 8

Solution().numSubarrayBoundedMax(nums, left, right)