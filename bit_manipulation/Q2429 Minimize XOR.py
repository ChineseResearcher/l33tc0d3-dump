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

    def minimizeXor(self, num1: int, num2: int) -> int:
        setBits = self.printInBinary(num2).count("1")

        ans = []
        for bit in self.printInBinary(num1):
            if bit == '1' and setBits > 0:
                setBits -= 1
                ans.append(bit)

            # 1) bit == '0'
            # OR 2) bit == '1' but no setBits left
            else:
                ans.append('0')

        # fill the remaining setbits from the right
        if setBits > 0:
            for i in range(len(ans)-1, -1, -1):
                if ans[i] == '0':
                    ans[i] = '1'
                    setBits -= 1

                    if setBits == 0: break

        return self.binaryToInt(''.join(ans), 32)

num1, num2 = 3, 5
num1, num2 = 1, 12

Solution().minimizeXor(num1, num2)