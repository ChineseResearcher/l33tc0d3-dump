# number theory - medium
class Solution:
    def concatenatedBinary(self, n: int) -> int:

        # key ideas:
        # 1) track accumulated bit_length of each i so as to determine 
        # the extent of left shifting << for each new i iterated
        # 2) add the left shifted value to our answer for every i
        # 3) for speed, use pow(base, exp, mod)

        ans, shift, MOD = 0, 0, int(1e9+7)
        for i in range(n, 0, -1):

            ans += i * pow(2, shift, MOD)
            shift += i.bit_length()

        return ans % MOD

n = 3
n = 12
n = int(1e5)

Solution().concatenatedBinary(n)