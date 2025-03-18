# bit manipulation - medium
class Solution:
    def longestNiceSubarray(self, nums):
        n = len(nums)
        # one key realisation is that for every pair of bitwise AND to
        # be zero in the subarr., the cumulative bitwise OR has to 
        # have no set bits overlap within itself

        l, windowOR = 0, 0

        # note that subarrays of length 1 are always considered nice
        ans = 1
        for r in range(n):

            # if the new element violates bitwise AND, shift left
            if (windowOR & nums[r]):

                while l < r and (windowOR & nums[r]):
                    # use bitwise XOR to undo bitwise OR with nums[l]
                    windowOR = windowOR ^ nums[l]
                    l += 1
                
                if l == r: windowOR = nums[r]

            # othwerwise we extend the window, and build on windowOR
            else:
                windowOR = windowOR | nums[r]

            ans = max(ans, r-l+1)

        return ans