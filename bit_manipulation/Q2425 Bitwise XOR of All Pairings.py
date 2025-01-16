# bit manipulation - medium
class Solution:
    def printInBinary(self, num, bit_length=32):
        bit_str = "{0:b}".format(num & (2**bit_length -1))
        bit_str = "0"*(bit_length-len(bit_str)) + bit_str
        return bit_str

    def binaryToInt(self, binary_str, bit_length):
        # Check if the sign bit is 1 (for negative numbers in two's complement)
        if binary_str[0] == '1':
            # If negative, find the two's complement (invert and add 1)
            unsigned_value = int(binary_str, 2)
            # Calculate the equivalent negative value
            signed_value = unsigned_value - (1 << bit_length)
        else:
            # If positive, just convert the binary to decimal
            signed_value = int(binary_str, 2)
        
        return signed_value

    def xorAllNums(self, nums1, nums2) -> int:
        n, m = len(nums1), len(nums2)
        # storing the count of '1' bit occurred at each bit_idx
        bit_map = {bit_idx: 0 for bit_idx in range(32)}

        # iterate through constant bit-length of 32 takes constant time
        for i in range(n):
            for idx, bit in enumerate(self.printInBinary(nums1[i])):

                if bit == '1': bit_map[idx] += m

        for j in range(m):
            for idx, bit in enumerate(self.printInBinary(nums2[j])):

                if bit =='1': bit_map[idx] += n

        ans = []
        for bit, freq in bit_map.items():

            if freq % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')

        return self.binaryToInt(''.join(ans), 32)
    
nums1, nums2 = [2,1,3], [10,2,5,0]
nums1, nums2 = [1,2], [3,4]

Solution().xorAllNums(nums1, nums2)