# dp - hard
from functools import cache
class Solution:
    def countNoZeroPairs(self, n: int) -> int:

        S = str(n)
        N = len(S)

        FULL_DIGI = list(map(int, '1234567890'))

        @cache
        def f(pos:int, carry:int, a_ended:bool, b_ended:bool) -> int:

            if pos == N:
                return 1 if carry == 0 else 0

            # determine the digits available depending on whether
            # part (a)/(b) has each ended or not
            digi_a = FULL_DIGI if not a_ended else [0]
            digi_b = FULL_DIGI if not b_ended else [0]

            # at first position cannot use 0 because we make sure
            # each part is a valid number instead of null
            if pos == 0:
                digi_a = digi_a[:-1]
                digi_b = digi_b[:-1]

            res = 0
            for a in digi_a:
                for b in digi_b:
                    if (a + b + carry) % 10 == int(S[N-pos-1]):
                        res += f(pos + 1,
                                (a + b + carry) // 10,
                                a_ended or (a == 0),
                                b_ended or (b == 0))

            return res

        return f(0, 0, False, False)
    
n = 10
n = 111
n = int(1e15)-1 # constraint

Solution().countNoZeroPairs(n)