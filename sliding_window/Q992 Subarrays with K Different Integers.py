# sliding window - hard
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        n = len(nums)
        # the challenge is to realise that the number of subarrays
        # with exactly k distinct numbers can be found via the following:
        # (1) number of subarrays with max. k distinct numbers
        # (2) number of subarrays with max. k-1 distinct numbers
        # ans = (1) - (2)

        # solve (1)
        l, part1 = 0, 0
        window = dict()
        for r in range(n):
            
            if nums[r] not in window:
                window[nums[r]] = 0
            window[nums[r]] += 1
            
            while len(window) > k:
                window[nums[l]] -=1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
                
            # after above while-filter, window
            # should contain at most k elements
            part1 += r - l + 1

        # solve (2)
        l, part2 = 0, 0
        window = dict()
        for r in range(n):
            
            if nums[r] not in window:
                window[nums[r]] = 0
            window[nums[r]] += 1
            
            while len(window) > k-1:
                window[nums[l]] -=1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
            part2 += r - l + 1
            
        return part1 - part2
    
nums, k = [1,2,1,2,3], 2
nums, k = [1,2,1,3,4], 3

Solution().subarraysWithKDistinct(nums, k)