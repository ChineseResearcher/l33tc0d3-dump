# number theory - hard
class Solution:
    def numberOfWays(self, corridor: str) -> int:

        n = len(corridor)
        # key ideas:
        # 1) since each partition needs to contain exactly 2 seats, there's
        # no way to form partitions with odd total count of seats
        # 2) by tracking the # of plants that are placed in between groups of 2 seats
        # we apply PnC to obtain the # of ways to partition
        seatCnt = corridor.count("S")
        if seatCnt == 0 or seatCnt % 2 == 1:
            return 0

        # first move the index to the end of first group of 2 seats
        seatCnt = 0
        for i in range(n):
            if corridor[i] == 'S':
                seatCnt += 1

            if seatCnt == 2:
                break

        ans, plantCnt, MOD = 1, 0, int(1e9+7)
        for j in range(i+1, n):
            if corridor[j] == 'S':
                seatCnt += 1

            if corridor[j] == 'P' and seatCnt == 2:
                plantCnt += 1

            if seatCnt > 2:
                ans *= (plantCnt + 1)
                ans %= MOD

                # reset
                plantCnt = 0 
                seatCnt %= 2

        return ans

corridor = "SSPPSPS"
corridor = "PPSPSP"
corridor = "S"
corridor = "P"

Solution().numberOfWays(corridor)