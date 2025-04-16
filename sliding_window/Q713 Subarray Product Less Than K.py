# sliding window - medium
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        l = 0

        ans, windowSumProd = 0, 1
        for r in range(n):
            
            windowSumProd *= nums[r]
            while windowSumProd >= k:
                
                if l > r:
                    break
                    
                windowSumProd /= nums[l]
                l += 1
                
            ans += max(r-l+1, 0)

        return ans
    
nums, k = [10,5,2,6], 100
nums, k = [1,2,3], 0

Solution().numSubarrayProductLessThanK(nums, k)