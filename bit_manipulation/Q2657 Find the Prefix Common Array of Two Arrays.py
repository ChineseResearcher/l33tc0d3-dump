# bit manipulation - medium
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        a, b = 0, 0
        
        ans = []
        for i in range(n):
            a |= (1 << A[i])
            b |= (1 << B[i])

            ans.append((a & b).bit_count())

        return ans

A, B = [1,3,2,4], [3,1,2,4]
A, B = [2,3,1], [3,1,2]

Solution().findThePrefixCommonArray(A, B)