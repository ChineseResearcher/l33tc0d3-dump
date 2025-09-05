# bit manipulation - medium
class Solution:
    def printInBinary(self, num, bit_length):
        bit_str = "{0:b}".format(num & (2**bit_length -1))
        bit_str = "0"*(bit_length-len(bit_str)) + bit_str
        return bit_str

    def find_next_toggle(self, n_left):
        zero_bits = 0
        while True:
        
            if n_left - 2 ** zero_bits <= 0:
                return zero_bits+1, n_left
        
            n_left -= 2 ** zero_bits
            zero_bits += 1

    def minEnd(self, n: int, x: int) -> int:

        # zero_to_toggle represents the 0-bits needed to be flip 1
        # counting from the right
        zero_to_toggle = []

        n -= 1 # x itself is a valid member

        while True:

            if n == 0:
                break

            next_toggle, n = self.find_next_toggle(n)
            zero_to_toggle.append(next_toggle)

            n -= 1

        base_binary_str = self.printInBinary(x, 128)
        zero_cnt, ans = 0, []
        for idx, char in enumerate(base_binary_str[::-1]):
            if char == '0':
                zero_cnt += 1
            if zero_cnt in zero_to_toggle:
                char = '1'

            ans.append(char)

        return int(''.join(ans[::-1]), 2)
    
n, x = 3, 4
n, x = 2, 7
n, x = 4, 1
n, x = 6, 1
n, x = 6715154, 7193485

Solution().minEnd(n, x)