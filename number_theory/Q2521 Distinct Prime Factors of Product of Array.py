# number theory - medium
from typing import List
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        # list down all prime factors (ignore freq) in O(sqrt(n)) time
        def unique_prime_factors(n):

            factors = set()
            # Check for factor 2
            if n % 2 == 0:
                factors.add(2)
                while n % 2 == 0:
                    n //= 2

            # Check for odd factors
            i = 3
            while i * i <= n:
                if n % i == 0:
                    factors.add(i)
                    while n % i == 0:
                        n //= i
                i += 2

            # If remaining n is a prime
            if n > 1:
                factors.add(n)

            return factors

        d_prime = set()
        for num in nums:
            d_prime |= unique_prime_factors(num)

        return len(d_prime)
    
nums = [2,4,8,16]
nums = [2,4,3,7,10,6]

Solution().distinctPrimeFactors(nums)