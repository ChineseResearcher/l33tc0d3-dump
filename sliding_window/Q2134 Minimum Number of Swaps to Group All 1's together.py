# sliding window - medium
class Solution:
    def minSwaps(self, nums):

        # handle special cases
        # case 1: all ones - already grouped
        if nums.count(1) == len(nums):
            return 0
        
        # case 2: only zeroes - no need to group
        if len(set(nums)) == 1 and set(nums).pop() == 0:
            return 0

        ones_cnt = nums.count(1)
        n = len(nums)
        min_moves = float('inf')

        # we construct a rolling window of 1s of size = ones_cnt
        # note that circular property is allowed
        # e.g., for ones_cnt = 3, [1, 0, ..., 0, 1, 1] is a valid window of ones grouped
        
        # to avoid recounting the zeros in each window of size = ones_cnt
        # we initiate a variable win_zero_cnt and keep track of it
        win_zero_cnt = nums[:ones_cnt].count(0)

        # case 3: already grouped in a fashion that is left bound 
        if win_zero_cnt == 0:
            return 0

        for left in range(1, n):
            right = (left + ones_cnt - 1) % n
            prev_left = left - 1

            # handle the left end
            if nums[prev_left] == 0:
                win_zero_cnt -= 1

            # handle the right end 
            if nums[right] == 0:
                win_zero_cnt += 1
            
            min_moves = min(min_moves, win_zero_cnt)

        return min_moves
    
nums = [0,1,0,1,1,0,0]
nums = [0,1,1,1,0,0,1,1,0]
nums = [1,1,0,0,1]
nums = [1,1,0,0]

Solution().minSwaps(nums)