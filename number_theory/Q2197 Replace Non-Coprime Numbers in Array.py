# number theory - hard
from typing import List
from functools import cache
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        # prime factorisation helper
        @cache
        def prime_fac(n: int) -> dict:

            fac = dict()

            # even factor 2
            if n % 2 == 0:
                fac[2] = 0
                while n % 2 == 0:
                    fac[2] += 1
                    n //= 2

            # odd factors
            i = 3
            while pow(i, 2) <= n:
                if n % i == 0:
                    fac[i] = 0
                    while n % i == 0:
                        fac[i] += 1
                        n //= i

                i += 2

            if n > 1:
                fac[n] = 1

            return fac

        n = len(nums)

        # stack init. w/ the first element
        st = [nums[0]]

        for i in range(1, n):

            # it is possible for sequential non-coprime to be detected
            curr = nums[i]
            while st:

                n1, n2 = st[-1], curr
                # results are cached to avoid redundant factorisation
                pf1, pf2 = prime_fac(n1), prime_fac(n2)
                common = pf1.keys() & pf2.keys()

                if not common:
                    break
                
                # have GCD > 1 and compute LCM
                # Note: a mathematical property exists where
                # GCD(x, y) * LCM(x, y) = x * y
                gcd = 1
                for fac in common:
                    gcd *= pow(fac, min(pf1[fac], pf2[fac]))

                lcm = (n1 * n2) // gcd
                curr = lcm
                st.pop()

            st.append(curr)

        return st
    
nums = [6,4,3,2,7,6,2]
nums = [2,2,1,1,3,3,3]
nums = [287,41,49,287,899,23,23,20677,5,825]

Solution().replaceNonCoprimes(nums)