# dp - medium
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for i in range(n)]

        # op1: multiple addition of the same single square number
        # e.g. 12 = 4 + 4 + 4
        for i in range(n):
            # identify a perfect square
            if int((i+1)**0.5)**2 == (i+1):
                dp[i] = 1

                j = 2
                while True:

                    if (i+1) * j > n:
                        break
                    dp[(i+1) * j - 1] = min(dp[(i+1) * j - 1], j)
                    j += 1

        # op2: a pair of square number
        # e.g. 13 = 9 + 4
        for i in range(n):
            
            # no point searching for numbers which are already perfect square itself
            if dp[i] != 1:
                # O(sqrt(N))
                for j in range(int((i+1) ** 0.5)):
                    dp[i] = min(dp[i], dp[(j+1)**2 - 1] + dp[(i+1) - (j+1)**2 - 1])

        return dp[-1]

n = 13
n = 34

Solution().numSquares(n)
