# dp - medium
from collections import defaultdict
divSet = defaultdict(list)
for i in range(1, 1001):
    for j in range(i + i, 1001, i):
        divSet[j].append(i)

class Solution:
    def minSteps(self, n: int) -> int:

        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) we can use DP and a O(n^2) process to compute dp[n]
        # 2) there are 2 types of transitions possible for some m < n:
        # - n % m = 0, then we can copy m, and paste (n // m) - 1 times to get n
        # - n = m * 2^k, then we can repeatedly copy and paste m for k times to get n
        # 3) we can pre-compute the divisible set of each number
        dp = [float('inf')] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            for d in divSet[i]:
                q = i // d
                dp[i] = fmin(dp[i], q + dp[d])
                # power of 2
                if q.bit_count() == 1:
                    k = q.bit_length() - 1
                    dp[i] = fmin(dp[i], 2 * k + dp[d])

        return dp[n]

n = 1
n = 3
n = 4
n = 9
n = 1000

Solution().minSteps(n)