# dp - medium
from typing import List
from functools import cache
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        n = len(matchsticks)
        # since all matchsticks have to be used, it total
        # length is not divisible by 4, early exit
        lengthAll = sum(matchsticks)

        if lengthAll % 4 != 0:
            return False

        sideLen = lengthAll // 4

        # knapsack pattern DP
        @cache
        def recursive_build(usage, sideLeft, currLen):

            if sideLeft == 0:
                return True
            
            res = False
            for pos in range(n):
                # get (valid) unused matchstick
                if usage & (1 << pos) == 0 and currLen + matchsticks[pos] <= sideLen:

                    nextLen = (currLen + matchsticks[pos]) % sideLen
                    # mark used
                    usage |= (1 << pos)
                    res |= recursive_build(usage,
                                        sideLeft-1 if nextLen == 0 else sideLeft,
                                        nextLen)
                    
                    # backtrack
                    usage &= ~(1 << pos)

                    # early stop
                    if res:
                        break

            return res

        return recursive_build(0, 4, 0)

matchsticks = [1,1,2,2,2]
matchsticks = [3,3,3,3,4]
# constraint
matchsticks = [4] * 15

Solution().makesquare(matchsticks)