# bit manipulation - medium
class Solution:
    def slide_window(self, window, new_bit):
        # Extract each bit from right to left
        second_bit = (window >> 1) & 1  # Middle bit
        first_bit = window & 1  # Rightmost in the window

        # Slide the window manually: '101' -> '01' + new_bit
        new_window = (second_bit << 2) | (first_bit << 1) | new_bit
        return new_window

    def minOperations(self, nums) -> int:
        n = len(nums)

        # init. '111' bitmask
        mask = int('111', 2)

        # fixed sliding window of size 3, interpreted as binary string
        window = int(''.join([str(d) for d in nums[:3]]), 2)

        ops = 0
        # if the third bit from right is 0 (or first bit in the window is 0)
        # we perform the operation to flip
        if window & 0b100 == 0:
            window = window ^ mask
            ops += 1

        for r in range(3, n):

            # slide the window manually with the new bit nums[r]
            window = self.slide_window(window, nums[r])

            # check if first bit in window is 0 bit
            if window & 0b100 == 0:
                # flip digits
                window = window ^ mask
                # increment ops
                ops += 1

        # we have to validate if the final window is all 1-bit
        if (window & 0b111) == 0b111:
            return ops
        else:
            return -1
        
nums = [0,1,1,1,0,0]
nums = [0,1,1,1]

Solution().minOperations(nums)