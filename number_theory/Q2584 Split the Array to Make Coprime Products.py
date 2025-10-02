# number theory - hard
from typing import List
from collections import defaultdict
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        
        n = len(nums)
        def unique_prime_factors(n:int) -> dict:

            factors = dict()
            # Check for factor 2
            if n % 2 == 0:
                factors[2] = 0
                while n % 2 == 0:
                    factors[2] += 1
                    n //= 2
                    
            # Check for odd factors
            i = 3
            while i * i <= n:
                if n % i == 0:
                    factors[i] = 0
                    while n % i == 0:
                        factors[i] += 1
                        n //= i
                i += 2

            # If remaining n is a prime
            if n > 1:
                factors[n] = 1

            return factors

        # since each number can be up to 1e6, cumulative product will blow up
        # thus we need to pre-process each number by prime-factorising it

        # there's no need to worry about inner-loop efficiency dealing with prime factors
        # as even the smallest 7 primes yield a cumulative prod. exceeding 1e6
        primeFac = [dict() for _ in range(n)]

        # build a cumulative suffix prime factor dict
        sf_prime = defaultdict(int)
        for i in range(n-1, -1, -1):
            primeFac[i] = unique_prime_factors(nums[i])

            for k, v in primeFac[i].items():
                sf_prime[k] += v

        # now iterate forward to find the smallest valid split
        # s.t. prefix cumulative prod. is co-prime of suffix cumulative prod.
        pf_prime = defaultdict(int)
        for i in range(n-1):

            # remove nums[i] from suffix prime
            for k, v in primeFac[i].items():
                sf_prime[k] -= v
                if sf_prime[k] == 0:
                    del sf_prime[k]

                pf_prime[k] += v

            # check for co-prime property:
            # no common prime factor
            if not pf_prime.keys() & sf_prime.keys():
                return i

        return -1

nums = [4,7,8,15,3,5]
nums = [4,7,15,8,3,5]

Solution().findValidSplit(nums)