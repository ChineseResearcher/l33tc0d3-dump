# array - easy
from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        n = len(bits)
        if n < 2:
            return True

        # if ends with [0,0], must be that last char is one-bit
        if bits[-2] == bits[-1] == 0:
            return True

        # otherwise, we have last two bits as [1,0]
        # iterate forward to validate if bits[:n-2] is proper
        ans, i = False, 0
        while i < n - 2:

            # in the forward scan, any '0' not preceded by '1' must be one-bit
            if bits[i] == 0:
                i += 1
                continue

            # otherwise for bits[i] = 1,
            # it must be grouped with the next bit, be it 0 / 1
            if i + 2 > n - 2:
                ans = True
                break

            i += 2

        return ans

bits = [1,0,0]
bits = [1,1,0]
bits = [1,1,1,0]

Solution().isOneBitCharacter(bits)