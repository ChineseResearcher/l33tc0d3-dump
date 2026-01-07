# dp - medium
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        # storing the glass status of glass ar row i col j
        # our tower is of height 100
        dp = [[0] * lvl for lvl in range(1, 101)] 

        dp[0][0] = poured
        # we don't have to really simulate till level 100
        # just up to the query_row would be enough
        for lvl in range(1, query_row+1):
            
            currLvl = dp[lvl-1]
            for col in range(lvl):
                glassHolding = currLvl[col]
                overflowed = (glassHolding - 1) / 2
                
                if overflowed > 0:
                    dp[lvl][col] += overflowed
                    dp[lvl][col+1] += overflowed

        return min(1, dp[query_row][query_glass])
    
poured, query_row, query_glass = 1, 1, 1
poured, query_row, query_glass = 2, 1, 1
poured, query_row, query_glass = 100000009, 33, 17

Solution().champagneTower(poured, query_row, query_glass)