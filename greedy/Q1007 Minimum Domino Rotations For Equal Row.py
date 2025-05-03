# greedy - medium
from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        # record the indices of dice num 1-6 for both top & bottom
        topIdx, botIdx = {i:set() for i in range(1, 7)}, {i:set() for i in range(1, 7)}

        for i in range(n):

            topIdx[tops[i]].add(i)
            botIdx[bottoms[i]].add(i)

        for dice, idxSet in sorted(topIdx.items(), key = lambda x: len(x[1]), reverse=True):
            if len(idxSet | botIdx[dice]) == n:
                return min(n - len(idxSet), n - len(botIdx[dice]))
        
        return -1
    
tops, bottoms = [2,1,2,4,2,2], [5,2,6,2,3,2]
tops, bottoms = [3,5,1,2,3], [3,6,3,3,4]

Solution().minDominoRotations(tops, bottoms)