# dp - hard
from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n, MOD = len(s), int(1e9 + 7)
        # we will just pre-compute any substring pattern (length <= 2)
        # involving "*" to make our life easier
        star = {
                # 1 '*': ver1
                '0*': 0, '1*': 9, '2*': 6, '3*': 0, '4*': 0,
                '5*': 0, '6*': 0, '7*': 0, '8*': 0, '9*': 0,
                # 1 '*': ver2
                '*1': 2, '*2': 2, '*3': 2, '*4': 2, '*5': 2,
                '*6': 2, '*7': 1, '*8': 1, '*9': 1, '*0': 2,
                '**': 15
                }

        @cache
        def recursive_decode(idx):

            if idx == n:
                return 1
            
            curr_res = 0
            # take one char:
            if s[idx] != '0':
                curr_res += ((9 if s[idx] == '*' else 1) * recursive_decode(idx+1) % MOD)

            # take two char:
            if idx < n-1 and s[idx] != '0':
                substring = s[idx:idx+2]
                if '*' in substring:
                    curr_res += (star[substring] * recursive_decode(idx+2)) % MOD
                else:
                    # purely digits
                    if int(substring) <= 26:
                        curr_res += recursive_decode(idx+2) % MOD

            return curr_res % MOD

        return recursive_decode(0)
    
s = "11106"
s = "1*"
s = "**"
s = "*" * 500

Solution().numDecodings(s)