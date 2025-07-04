# recursion - hard
import math
from typing import List
from string import ascii_lowercase as lwc
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        # record the net shifts from "a"
        # i.e. shift = 1 means "b", shift = 2 means "c"
        curr, shift = k, 0

        # the core idea is to track many shifts have been applied
        # to the k-th character by observing the relationship between
        # the floor division res. and the correct index to access operations

        # even though there's no recursion directly applied
        # the spirit is such that we are reducing our problem space
        # by making correct reductions on "curr"
        # i.e. for the length-16 string "aabbaabbbbccbbcc"
        # the 15-th char. "c" is impacted by the 7th char. "b" (think mirroring)
        # and the 7th char. "b" is impacted by the 3rd char. "b"
        # and the 3rd char. "b" is impacted by the 1st char. "a"
        while curr > 1:

            # perform floor division on curr
            fd = int(math.log(curr) // math.log(2))

            idx, pow_res = fd, 2 << (fd - 1)
            if curr == pow_res:
                idx -= 1

            shift += operations[idx]
            curr -= (2 << (idx-1) if idx > 0 else 1)

        return lwc[shift % 26]
    
k, operations = 5, [0,0,0]
k, operations = 10, [0,1,0,1]
k, operations = 4, [1,0]
k, operations = int(1e14), [1] * 100 # constraint

Solution().kthCharacter(k, operations)