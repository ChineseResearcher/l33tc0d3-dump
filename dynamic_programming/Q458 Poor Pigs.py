# dp - hard
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

        R = minutesToTest // minutesToDie
        # design the states as p: pig count, r: round cnt
        # where dp[p][r] would refer to the number of buckets that could be
        # determined if it contains poison given p pigs and r rounds

        # goal is to find the smallest number of pigs required s.t.
        # dp[p][r] >= buckets

        # since we do not know the optimal p to begin with, we
        # keep expanding and overriding our dp table as we add an additional pig

        # w/ no pigs, we could only determine up to 1 bucket
        dp, pigCnt = [1] * (R+1), 0

        while True:

            # for the curr. pigCnt, if we test for R rounds
            # we would be able to discern enough buckets
            if dp[R] >= buckets:
                break

            # the transitions into dp[p][r] is:
            # dp[p][r] = dp[p-1][r] * (r+1)
            # interpretation: w/ the additional pig, which itself encodes (r+1) states
            # i.e., fail at 1st rnd, fail at 2nd rnd, ..., fail at r-th rnd, survive ALL
            # we multiply this w/ the previous dp[p-1][r]

            new_dp = []
            for rnd in range(R+1):
                new_dp.append(dp[rnd] * (rnd + 1))

                # early stop if we hit above buckets before r = R
                if new_dp[-1] >= buckets:
                    return pigCnt + 1

            # override: dp[p][0...R] becomes dp[p+1][0...R] 
            dp = new_dp
            pigCnt += 1

        return pigCnt
    
buckets, minutesToDie, minutesToTest = 4, 15, 15
buckets, minutesToDie, minutesToTest = 4, 15, 30
buckets, minutesToDie, minutesToTest = 1000, 15, 60

Solution().poorPigs(buckets, minutesToDie, minutesToTest)