# dp - hard
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = int(1e9 + 7)
        # since there are five vowels: a, e, i, o, u
        # init. 2-D dp of size n x 5
        dp = [ [0] * 5 for _ in range(n) ]

        # when n = 1, there's only one possible string ending
        # at each vowel so we mark first row as 1s
        for c in range(5):
            dp[0][c] = 1

        for r in range(1, n):

            # the transitions can be captured via description
            # 'a' transitioned from 'e', 'i' & 'u'
            dp[r][0] = (dp[r-1][1] + dp[r-1][2] + dp[r-1][4]) % MOD

            # 'e' transitioned from 'a' & 'i'
            dp[r][1] = (dp[r-1][0] + dp[r-1][2]) % MOD

            # 'i' transitioned from 'e' & 'o'
            dp[r][2] = (dp[r-1][1] + dp[r-1][3]) % MOD

            # 'o' transitioned from 'i' 
            dp[r][3] = dp[r-1][2] % MOD

            # 'u' transitioned from 'i' & 'o'
            dp[r][4] = (dp[r-1][2] + dp[r-1][3]) % MOD

        return sum(dp[-1]) % MOD
    
n = 2 # "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua"
n = int(1e5)

Solution().countVowelPermutation(n)