# number theory - medium
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        # key ideas:
        # 1) to bring the cost down, we need to make 
        # use of our startingAt position as much as possible
        # e.g. 369 seconds can be more optimally typed with "569" instead
        # of "609" if we happen to start at "5"

        # 2) process the targetSeconds and output typing sequence(s)
        # including the alternative made possible by (1)
        ans = float('inf')

        formatMin = lambda x: str(x) if x > 0 else ''
        formatSec = lambda x: str(x).rjust(2, '0') 

        def cost(seq: str) -> int:
            if len(seq) > 4 : return float('inf') 
            res = pushCost if int(seq[0]) == startAt else pushCost + moveCost
            for i in range(1, len(seq)):
                if seq[i] != seq[i-1]:
                    res += moveCost
                res += pushCost
            return res

        # first compute the naive option
        minutes = formatMin(targetSeconds // 60)
        seconds = formatSec(targetSeconds % 60)
        seq = (minutes + seconds).lstrip('0')
        ans = min(ans, cost(seq))

        # second option is to maximise the seconds used (up to 99)
        minutes = 0
        while targetSeconds - minutes * 60 > 99:
            minutes += 1
        seconds = formatSec(targetSeconds - minutes * 60)
        minutes = formatMin(minutes)
        seq = (minutes + seconds).lstrip('0')
        ans = min(ans, cost(seq))

        # third option is to re-use startAt if possible
        if startAt > 0:
            for minutes in [startAt] + \
                        [int(str(startAt) + str(x)) for x in range(0, 10)]:
                seconds = targetSeconds - minutes * 60
                if 0 <= seconds <= 99:
                    ans = min(ans, cost(formatMin(minutes) + formatSec(seconds)))
                    break
        
        return ans

startAt, moveCost, pushCost, targetSeconds = 1, 2, 1, 600
startAt, moveCost, pushCost, targetSeconds = 5, 2, 1, 369
startAt, moveCost, pushCost, targetSeconds = 0, 1, 2, 76
startAt, moveCost, pushCost, targetSeconds = 0, 1, 4, 9
startAt, moveCost, pushCost, targetSeconds = 1, 9403, 9402, 6008

Solution().minCostSetTime(startAt, moveCost, pushCost, targetSeconds)