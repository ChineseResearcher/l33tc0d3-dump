# string - medium
import math
class Solution:
    def numSub(self, s: str) -> int:
        
        MOD = int(1e9) + 7 
        # track number of contiguous 1s
        o, ans = 0, 0
        for char in s:
            if char == '1':
                o += 1
            else:
                ans += math.comb(o+1, 2)
                ans %= MOD
                o = 0 # reset

        # in case last char is "1", collect it
        if o > 0:
            ans += math.comb(o+1, 2)

        return ans % MOD

s = "101"
s = "0110111"
s = "111111"

Solution().numSub(s)