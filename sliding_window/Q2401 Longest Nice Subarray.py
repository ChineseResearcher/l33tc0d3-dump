# sliding window
class Solution:
    def printInBinary(self, num, bit_length=32):
        bit_str = "{0:b}".format(num & (2**bit_length -1))
        bit_str = "0"*(bit_length-len(bit_str)) + bit_str
        return bit_str

    def longestNiceSubarray(self, nums):
        n = len(nums)
        # use a sliding window to find the longest subarr. in which the freq. of bit pos
        # should not exceed 1 to ensure any pairs would not give bit-AND != 0
        window_dict = {i:0 for i in range(32)}

        # ans is default to 1
        l, ans = 0, 1
        for r in range(n):

            num = nums[r]
            
            # record the bit pos. which have more than 1 occurrence
            violation = set()
            for bit_pos, bit in enumerate(self.printInBinary(num)):
                window_dict[bit_pos] += int(bit)

                if window_dict[bit_pos] > 1: violation.add(bit_pos)
            
            while violation:
            
                for bit_pos, bit in enumerate(self.printInBinary(nums[l])):
                    if bit == '1': 
                        window_dict[bit_pos] -= 1

                    if window_dict[bit_pos] <= 1:
                        violation.discard(bit_pos)

                l += 1

            ans = max(ans, r-l+1)

        return ans
    
nums = [1,3,8,48,10]
nums = [3,1,5,11,13]

Solution().longestNiceSubarray(nums)