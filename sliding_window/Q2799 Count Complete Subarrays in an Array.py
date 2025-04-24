# sliding window - medium
class Solution:
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        # count total distinct elements
        k = len(set(nums))

        # maintain a window set
        window = dict()

        l, completeCnt = 0, 0
        for r in range(n):
            
            if nums[r] not in window:
                window[nums[r]] = 0
                
            window[nums[r]] += 1
            # shrink the left end if possible
            while len(window) == k:

                # realise that if nums[l:r+1] is already complete
                # then it holds true for nums[l:j] for j in [r+2, n]
                completeCnt += n - r
                
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1

        return completeCnt
    
nums = [1,3,1,2,2]
nums = [5,5,5,5]

Solution().countCompleteSubarrays(nums)