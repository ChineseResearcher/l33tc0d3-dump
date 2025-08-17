# dp - medium
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        if k == 0:
            return 1

        dp = [None] * (n+1)
        # first proba. should be assigned to subproblem (1+(n-k), 1)
        if maxPts <= 1 + (n-k):
            return 1

        dp[1 + (n-k)] = (1 + (n-k)) / maxPts
        for i in range(1 + (n-k)):
            dp[i] = 1

        # update dp[i] w/ a sliding window sum
        windowSum, l = sum(dp[:1+(n-k)+1]), 0
        for i in range(1+(n-k)+1, n+1):

            r = i-1
            # at each i, dp[i] will inherit from the past k
            # consecutive dp values, where m is the smaller of (i, maxPts)
            m = min(i, maxPts)

            # we need to keep excluding dp[l] as long as
            # the window length represented by r-l+1 exceeds "m" 
            while r-l+1 > m:
                windowSum -= dp[l]
                l += 1

            dp[i] = windowSum / maxPts
            # accumulate curr. dp[i] to windowSum
            windowSum += dp[i]

        return dp[-1]
    
n, k, maxPts = 21, 17, 6
n, k, maxPts = 6, 1, 10
n, k, maxPts = 0, 0, 2
n, k, maxPts = 1001, 500, 502
n, k, maxPts = 1001, 500, 503
n, k, maxPts = 10000, 5000, 5002 # constraint

Solution().new21Game(n, k, maxPts)