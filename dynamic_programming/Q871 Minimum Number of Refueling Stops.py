# dp - hard
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        
        if not stations: return 0 if startFuel >= target else -1

        n = len(stations)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) dp[r][i] denotes the max. reachable dist. after making "r" refuels
        # and considering up to station "i" 
        # 2) the "take" transition resembles jump game II, except that a new dist. is
        # based on dp[r - 1][i - 1] + stations[i][1] instead of stations[i][0] + stations[i][1]

        dp = [ [0] * (n + 1) for _ in range(n + 1) ]
        # if 0 refuel, the max. dist. is equivalent to startFuel
        for i in range(n + 1):
            dp[0][i] = startFuel

        for i in range(1, n + 1):
            for r in range(1, i + 1):
                # skip option
                dp[r][i] = dp[r][i - 1]
                # take option: subject to coverage check
                if dp[r - 1][i - 1] >= stations[i - 1][0]:
                    dp[r][i] = fmax(dp[r][i], dp[r - 1][i - 1] + stations[i - 1][1])

        # enumuerate r in [0...n] s.t. dp[r][n] >= target
        for r in range(n + 1):
            if dp[r][n] >= target:
                return r

        return -1

target, startFuel, stations = 1, 1, []
target, startFuel, stations = 100, 1, [[10,100]]
target, startFuel, stations = 100, 10, [[10,60],[20,30],[30,30],[60,40]]
target, startFuel, stations = 1000, 299, [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]

Solution().minRefuelStops(target, startFuel, stations)