# two pointer - easy
class Solution:
    # implemented in O(n) time and O(1) space as a challenge
    def applyOperations(self, nums):
        n = len(nums)

        # perform operations as described
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        # # we keep to pointer for the rightmost index we could place a 0
        zero_idx = 0
        for i in range(n):
            if nums[i] != 0:
                while zero_idx < i and nums[zero_idx] != 0:
                    zero_idx += 1

                if zero_idx < i and nums[zero_idx] == 0:
                    nums[zero_idx] = nums[i]
                    nums[i] = 0
                    zero_idx += 1

        return nums
    
nums = [0,1]
nums = [1,2,2,1,1,0]
nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]

Solution().applyOperations(nums)