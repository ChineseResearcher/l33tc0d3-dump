# greedy - medium
class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        m = n // 2
        # key ideas:
        # 1) when there are unsolved "?" on both sides, it is optimal for both 
        # alice and bob to pick 9 and add to the respective sides. In particular,
        # alice would add to the side w/ larger sum, and bob would add to the other

        # 2) we can cancel out the "?"s on both sides, and if there are still "?"s
        # remaining on either side, we can determine the outcome by enumeration

        # 3) suppose alice has r1 "?"s and bob has r2 "?"s to address after cancelling,
        # and that the diff between left and right partition is k:
        # (i)   if r1 * 9 > k: alice picks 9 r1 times, which surely exceeds diff no matter
        # what bob chooses, i.e. alice wins
        # (ii)  if r1 * 9 <= k and r2 * 9 < k: alice picks 0 r1 times, leaving bob with no
        # possibility of amounting to diff even if he maxes out by picking 9 r2 times
        # (iii) if r1 * 9 = k and r2 * 9 = k (i.e. r1 = r2): no matter what alice picks, 
        # bob will be able to complement each choice alice makes to add up 9, and diff
        # is reduced exactly to 0, bob wins

        lSum, lCnt, rSum, rCnt = 0, 0, 0, 0
        for i in range(n):
            if num[i] == '?':
                if i < m:
                    lCnt += 1
                else:
                    rCnt += 1
            else:
                if i < m:
                    lSum += int(num[i])
                else:
                    rSum += int(num[i])

        t = min(lCnt, rCnt)
        lCnt -= t
        rCnt -= t

        if lCnt == rCnt == 0: return True if lSum != rSum else False

        if lCnt > 0:
            diff = rSum - lSum
        else:
            diff = lSum - rSum

        c = max(lCnt, rCnt)
        alice_rem = (c // 2) + (c % 2)
        bob_rem = c // 2

        if alice_rem * 9 > diff:
            return True
        else:
            if bob_rem * 9 == diff:
                return False
            elif bob_rem * 9 < diff:
                return True

num = "5023"
num = "25??"
num = "?3295???"

Solution().sumGame(num)