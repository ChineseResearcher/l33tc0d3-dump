# sliding window - hard
class Solution:
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        # maintain a (lazy) sliding window where elements in nums[l:r+1] 
        # are strictly within [minK, maxK] but not necessarily containing minK and/or maxK
        l, minK_idx, maxK_idx = 0, None, None

        ans = 0
        for r in range(n):

            # for out-of-bound elements we immediately invalidate
            # the curr. window by letting l > r
            if nums[r] > maxK or nums[r] < minK:
                l = r + 1
                # reset minK_idx, maxK_idx
                minK_idx, maxK_idx = None, None

            if nums[r] == maxK:
                maxK_idx = r
            
            if nums[r] == minK:
                minK_idx = r

            # validate if we have an active window
            if r >= l:
                
                # validate if curr. active window is bounded exactly
                if minK_idx is not None and maxK_idx is not None:
                    ans += min(minK_idx, maxK_idx) - l + 1

        return ans
    
nums, minK, maxK = [1,3,5,2,7,5], 1, 5
nums, minK, maxK = [1,1,1,1], 1, 1
nums, minK, maxK = [0,3,3,1,5,1,4,4], 1, 5

Solution().countSubarrays(nums, minK, maxK)