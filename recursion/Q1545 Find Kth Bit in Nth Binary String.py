# recursion - medium
import math
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        # the middle mirroring bit "1" would always be the
        # 2nd, 4th, 8th, 16th...2^k-th number
        # hence first check for the special case of k being a power of 2
        if k > 1 and not (k & (k-1)):
            return "1"

        curr, invertCnt = k, 0
        while curr > 1:

            invertCnt += 1
            # first ascertain for the curr "k", what's the bounding n
            fd = int(math.log(curr) // math.log(2))
            s_len = (2 << fd) - 1

            # mirror reduction on curr "k", i.e. undo reverse()
            curr = s_len - curr + 1

            # it "k" is reduced to a perfect power of 2
            # we shall early return based on invertCnt
            if curr > 1 and not (curr & (curr-1)):
                return "1" if not (invertCnt % 2) else "0"

        return "0" if not (invertCnt % 2) else "1"
    
n, k = 3, 6
n, k = 4, 11
n, k = 20, 2 << 19

Solution().findKthBit(n, k)