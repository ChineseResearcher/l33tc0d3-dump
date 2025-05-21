# dp - medium
from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # since input size of 1e5, the dp algorithm should be linear
        dp = [0] * (n+1)
        dp[1] = 1

        # the main question is:
        # at dp[i], which previous state(s) do we need to make use of ??
        # we can't be traversing through all previous states as that would be O(n^2)
        # the answer lies in creating an auxiliary pointers arr. that
        # indicates which prev. dp states should primes be pointing to compute the i-th smallest SUN
        # note: pointers all init. to 1, referring to dp[1] (dp[1] = 1), which implies
        # that at the starting round, we obtain the (2nd) smallest SUN by
        # [1*primes[0], 1*primes[1], ..., 1*primes[m-1]]
        m = len(primes)
        pointers = [1] * m

        for i in range(2, n+1):

            curr_sun = float('inf')
            for j in range(m):

                number = primes[j] * dp[pointers[j]]
                if number < curr_sun:
                    # we need to record the index k where
                    # the smallest SUN is achieved
                    curr_sun = number

            dp[i] = curr_sun
            # a critical operation is that for the corresponding
            # indices (possibly more than 1) of curr SUN, it now gets shifted by one
            # i.e. pointing to the next larger do val. to generate the next potential SUN
            for j in range(m):
                if primes[j] * dp[pointers[j]] == curr_sun:
                    pointers[j] += 1
                    
        return dp[-1]
    
n, primes = 12, [2,7,13,19]
n, primes = 1, [2,3,5]
# constraints
n, primes = int(1e5), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

Solution().nthSuperUglyNumber(n, primes)