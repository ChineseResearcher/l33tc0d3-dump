# dp - hard
from functools import cache
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:

        if n == 0:
            return 0
        
        @cache
        def f(n):

            bit_cnt, bit_len = n.bit_count(), n.bit_length()    
            # obtain the set bit positions
            sb = []
            for i in range(bit_len-1, -1, -1):
                if n & (1 << i):
                    sb.append(i)

            # the optimal reduction operations to reduce 2^k to 0
            # is always 2^(k+1) - 1 by induction
            if bit_cnt == 1:
                return pow(2, sb[0] + 1) - 1
            
            # otherwise at least two bits
            # case 1: first two set bits (from right) are consecutive
            if sb[-1] + 1 == sb[-2]:

                # two options:
                # 1) invert sb[-2]
                op1 = 1 + f(n ^ (1 << sb[-2]))
                # 2) keep sb[-2] and reduce sb[-1]
                op2 = pow(2, sb[-1] + 1) - 1 + f(n ^ (1 << sb[-1]))

                return min(op1, op2)
            
            # case 2: non-consecutive
            else:

                # two options:
                # 1) reduce sb[-1] directly
                op1 = pow(2, sb[-1] + 1) - 1 + f(n ^ (1 << sb[-1]))
                # 2) first invert sb[-1] + 1 to a set bit, then reduce sb[-1] 
                new_n = n ^ (1 << (sb[-1] + 1)) ^ (1 << sb[-1])
                op2 = pow(2, sb[-1] + 1) + f(new_n)

                return min(op1, op2)

        return f(n)
    
n = 3 
n = 6
# constraint
n = int(1e9)

Solution().minimumOneBitOperations(n)