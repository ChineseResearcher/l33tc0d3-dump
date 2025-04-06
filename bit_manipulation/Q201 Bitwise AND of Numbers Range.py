# bit manipulation - medium
import math
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0: return 0
        if left == right: return left

        lb_max_setbit = int(math.log(left) / math.log(2))
        rb_max_setbit = int(math.log(right) / math.log(2))

        # if the max. set bit of right bound is larger than that of left
        # we can be guaranteed that at least one occurrence of 0-bit occurs
        # at every bit position possible, making bitwise AND 0
        if rb_max_setbit > lb_max_setbit:
            print('case1')
            return 0

        # otherwise, if max. set bit of left & right are the same
        # we could test for any bit pos < max_setbit if a set bit would at least be unset once

        # the idea is the following:
        # for any 0-bit, all the 1-bits (if any) to the right would be unset at least once
        # we could define a valid set that records the 1-bits before any 0-bit is seen
        valid = set() 
        for pos in range(lb_max_setbit-1, -1, -1):
            # if we encounter the 0-bit s.t. by setting this bit it won't exceed right
            # we've found the first 0-bit that would invalidate all 1-bits (if any) to the right
            if left & (1 << pos) == 0:
                sentinel = 0 | (1 << lb_max_setbit) | (1 << pos)
                for vp in valid:
                    sentinel |= (1 << vp)

                if sentinel <= right:
                    break

            if left & (1 << pos) != 0:
                valid.add(pos)

        # append max setbit to valid
        valid.add(lb_max_setbit)
        ans = 0
        for pos in valid:
            ans += 1 << pos

        return ans 
    
left, right = 5, 7
left, right = 5, 6
left, right = 26, 27
left, right = 111, 127
left, right = 107, 111
left, right = 2 ** 30 + 99999999, 2**31 -1

Solution().rangeBitwiseAnd(left, right)