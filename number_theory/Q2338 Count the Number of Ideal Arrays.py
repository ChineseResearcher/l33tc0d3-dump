# number theory - hard
import math
class Solution:
    def prime_factorisation(self, num):
        # given a integer num, deconstruct the integer into
        # its prime factorisation, e.g. 24 = 2^3 * 3
        # so we return [(2,3),(3,1)]
        if num < 2:
            return []
        
        searchRange = [2] + [x for x in range(3, int(num ** 0.5) +1)]
        
        pf = []
        for divisor in searchRange:
            
            if num % divisor == 0:
                p_cnt = 0
                while num >= divisor and num % divisor == 0:
                    p_cnt += 1
                    num //= divisor
                pf.append((divisor, p_cnt))
            
            if num == 1:
                break
                
        if num != 1:
            pf.append((num, 1))
                
        return pf

    def idealArrays(self, n: int, maxValue: int) -> int:

        MOD = int(1e9 + 7)
        # idea is to iterate through [1, maxValue] and find the number
        # of ideal arrays if we are ending at the iterated x
        idealArrCnt = 0
        for x in range(1, maxValue + 1):
            # get the prime factor representation in O(sqrt(x)) time
            pf = self.prime_factorisation(x)
            
            # to count for ending at x, we can model it as a combinatorics
            # problem where each of its prime factors (possible multiple occurrrences)
            # can be arranged into the n buckets
            
            # because the distribution of a prime factor
            # is independent from one another as we do not impose restrictions
            # on the order of the prime factors within a "bucket", 
            # multiplication rule applies
            mul = 1
            for prime, freq in pf:
                # form n buckets
                # the problem is tagged DP because nCk can be sped-up
                # using DP, see Pascal's Triangle
                mul *= math.comb(n+freq-1, freq)
                mul %= MOD
            
            idealArrCnt += (mul % MOD)
            
        return idealArrCnt % MOD
    
n, maxValue = 2, 5
n, maxValue = 5, 3
n, maxValue = 184, 389

Solution().idealArrays(n, maxValue)