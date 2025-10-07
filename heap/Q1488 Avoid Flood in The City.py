# heap - medium
from typing import List
import heapq
from collections import defaultdict
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]: 

        n = len(rains)

        # iterate backwards and store the days on which rains[i] lake would
        # receive rainfall in a hashmap idenfified by key = rains[i]
        haveRain = defaultdict(list)

        for i in range(n-1, -1, -1):
            if rains[i] > 0:
                haveRain[rains[i]].append(i)

        # build a minheap storing <rainDay, lake>
        # so that we always get the optimal lake to dry first
        toDry = []

        ans, full = [], set()
        for i in range(n):

            curr = rains[i]
            if curr != 0:

                # rain on an already full lake
                if curr in full:
                    ans = []
                    break

                full.add(curr)
                ans.append(-1)
                # depending on whether this lake would receive further rainfall
                # push the info into the minheap for optimal drying
                haveRain[curr].pop()
                if haveRain[curr]:
                    heapq.heappush(toDry, (haveRain[curr][-1], curr))

            # drying operation
            else:

                # get the lake to dry (if there's full lake)
                if not toDry:
                    ans.append(1) # any lake is ok
                    continue

                _, lake = heapq.heappop(toDry)
                full.discard(lake)
                ans.append(lake)

        return ans
    
rains = [1,2,3,4]
rains = [1,2,0,1,2]
rains = [1,2,0,0,2,1]
rains = [1,2,0,3,2,0,1]

Solution().avoidFlood(rains)