# dp - medium
from collections import deque
# O(n^2) ver.
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # dp[i][j] is the number of people knowing the secret on day i
        # and that j days have passed since they know that secret
        # dp = [ [0] * forget for _ in range(n) ]

        # we could optimise the above by reducing it to 1D
        # where we only keep the latest dp[day]
        dp = [0] * forget

        # on the first day, only person A (first person) knows the secret
        dp[0] = 1

        # second day onwards
        MOD = int(1e9 + 7)
        for day in range(1, n):

            new_cnt, new_dp = 0, [0] * forget
            for k in range(1, forget):
                new_dp[k] = dp[k-1]
                if k >= delay:
                    new_cnt += new_dp[k]

            # new people who get to know the secret today
            new_dp[0] = new_cnt % MOD
            # space optimisation
            dp = new_dp 

        return sum(dp) % MOD
    
# O(n) ver.
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # dp[i][j] is the number of people knowing the secret on day i
        # and that j days have passed since they know that secret
        # dp = [ [0] * forget for _ in range(n) ]

        # we could optimise the above by using a queue-based dp
        dp, qSum = deque([1] + [0] * (forget-1)), 0

        # second day onwards
        MOD = int(1e9 + 7)
        for day in range(1, n):

            # increment qSum by the number of sharings that would
            # occur today as a result of crossing over the delay
            qSum += dp[delay-1]

            # decrement qSum because it hits forget day
            qSum -= dp.pop()
            
            qSum %= MOD
            dp.appendleft(qSum)

        return sum(dp) % MOD
    
n, delay, forget = 7, 2, 4
n, delay, forget = 4, 1, 3
n, delay, forget = 1000, 500, 999 # constraint

Solution().peopleAwareOfSecret(n, delay, forget)