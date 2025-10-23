# number theory - hard
import math
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        # the key to solving this problem is to see how the process is
        # like traversing the INVERTED Pascal's triangle
        # where the n-th row with coefficients nC1, nC2, ..., nCn
        # denotes how many times the i-th value in the n-th row contributes
        # to the bottom single value

        # since we are interested in the second last row (row with two elements)
        # where we denote the two values as val1, val2
        # the n-th row values contribute to val1 & val2 in such a way:
        #    1) the first n-1 values in n-th row contribute to val1
        #    2) the last n-1 values in n-th row contribute to val2
        #    3) the coeff. of contributions are coeff. in the "n-1"-th row of Pascal triangle
        val1, val2 = 0, 0

        # since "n" can get up tp 1e5, we need an efficient way 
        # of computing the binomial coeff. in the "n-1"-th row
        n = len(s)

        # solution?
        # Lucas Theorem + Chinese Remainder Theorem (CRT)
        def nCr_mod_p_lucas(n, r, p):
            '''
            Compute nCr mod p (where n, r could be large) using Lucas Theorem
            '''
            # Note: math.comb(n, r) % p is efficient up to n = 1e5, so we need Lucas
            # to handle even larger n for efficiency
            res = 1
            while n > 0 or r > 0:
                # in Lucas Theorem, both "n" and "r" are re-expressed in base-p (p is prime)
                # e.g. n = n_1 * p + n_2 * p^2 + n_3 * p^3 + ....
                n_i, r_i = n % p, r % p
                # we can safely call math.comb here because both
                # n_i and r_i are in the range [0, p-1] as they are modulo results
                # and in our case the p supplied is either 2 or 5
                res *= math.comb(n_i, r_i) % p
                res %= p
                n //= p
                r //= p

            return res % p

        def crt_two(a1, m1, a2, m2):
            '''
            CRT states that given:
            X ≡ a1 (mod m1), and X ≡ a2 (mod m2), where m1, m2 are co-primes
            There exists a unique X s.t. :
            X ≡ (a1 * M1 * M1_inv + a2 * M2 * M2_inv) mod M 
            where M = m1 * m2; M1 = M // m1; M2 = M // m2
            '''
            M = m1 * m2
            M1, M2 = M // m1, M // m2
            # modular arithmetic for inverse of M1 & M2
            inv1 = pow(M1, -1, m1)
            inv2 = pow(M2, -1, m2)
            return (a1 * M1 * inv1 + a2 * M2 * inv2) % M

        def nCr_mod_10(n, r):
            a1 = nCr_mod_p_lucas(n, r, 2)
            a2 = nCr_mod_p_lucas(n, r, 5)
            return crt_two(a1, 2, a2, 5)

        # now with Lucas-based nCr mod p implemented, 
        # we can find out the binom coeff for the "n-1"-th row
        binom = [nCr_mod_10(n-2, r) for r in range(0, n-1)]

        val1, val2 = 0, 0
        for i in range(len(binom)):
            val1 += int(s[i]) * binom[i]
            val2 += int(s[n-i-1]) * binom[i]

        val1 %= 10
        val2 %= 10

        return val1 == val2
    
s = "3902"
s = "34789"
# constraint
s = "1" * int(1e5)

Solution().hasSameDigits(s)