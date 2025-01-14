# bit manipulation - medium
class Solution:
    # runs in O(N)
    def printInBinary(self, num, bit_length):
        bit_str = "{0:b}".format(num & (2**bit_length -1))
        bit_str = "0"*(bit_length-len(bit_str)) + bit_str
        return bit_str
        
    def findThePrefixCommonArray(self, A, B):
        # both A, B have same length
        n = len(A)

        # initiate two dummy bitmasks
        a, b = 0, 0

        ans = []
        for i in range(n):

            # set bits according to number read in
            a |= (1 << A[i])
            b |= (1 << B[i])

            ans.append(self.printInBinary(a & b, n+1).count('1'))

        return ans
    
A, B = [1,3,2,4], [3,1,2,4]
A, B = [2,3,1], [3,1,2]

Solution().findThePrefixCommonArray(A, B)