# number theory - hard
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        MOD = int(1e9 + 7)
        # similar to Q3343, as both potentially deal w/ very large nCk
        # use Fermat's little theorem to speed up the nCk part gives significant speed advantage

        # pre-compute fact and invFact
        fact = [1] * (n+1)
        invFact = [1] * (n+1)

        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD

        invFact[n] = pow(fact[n], MOD-2, MOD) # fermat's
        for j in range(n-1, 0, -1):
            invFact[j] = invFact[j+1] * (j+1) % MOD

        def comb(n, k):
            return fact[n] * (invFact[k] % MOD) * (invFact[n-k] % MOD)

        # first position have m choices
        ans = m

        # for the next n-1 positions, we choose k places to have equal adjacents
        ans *= comb(n-1, k)

        # then the remaining positions have to all have arr[i] != arr[i-1]
        ans *= pow((m-1), (n-k-1), MOD)

        return ans % MOD
    
n, m, k = 3, 2, 1
n, m, k = 4, 2, 2
n, m, k = 5, 2, 0
n, m, k = 40603, 16984, 29979
n, m, k = 28634, 7068, 10100

Solution().countGoodArrays(n, m, k)