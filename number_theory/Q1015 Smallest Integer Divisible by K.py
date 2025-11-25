# number theory - medium
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        # init. dividend as 1, and increment "1" usage along the way
        dividend, ans = 1, 1

        # keep track of seen dividend
        seen = set()
        while True:

            while dividend < k:
                dividend = dividend * 10 + 1
                ans += 1 # usage incremented

            if dividend in seen:
                ans = -1
                break

            seen.add(dividend)

            # perform division
            dividend = dividend % k

            # is divisible at some point
            if dividend == 0:
                break

        return ans

k = 1
k = 2
k = 99999

Solution().smallestRepunitDivByK(k)