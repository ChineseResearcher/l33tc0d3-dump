# heap - medium
import heapq
from typing import List
from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        freq = Counter(barcodes)

        # construct a max-heap based on <freq, number>
        maxheap = []
        for num, f in freq.items():
            heapq.heappush(maxheap, [-f, num])

        ans = []
        while maxheap:

            if not ans:
                f, num = heapq.heappop(maxheap)
                ans.append(num)
                if f + 1 < 0:
                    heapq.heappush(maxheap, [f+1, num])

                continue
            
            # get the number w/ the most count left
            # if it collides w/ the previous selection, skip once
            snum = -1
            if ans[-1] == maxheap[0][1]:
                sf, snum = heapq.heappop(maxheap)

            f, num = heapq.heappop(maxheap)
            ans.append(num)
            if f + 1 < 0:
                heapq.heappush(maxheap, [f+1, num])

            if snum > -1:
                heapq.heappush(maxheap, [sf, snum])

        return ans
    
barcodes = [1,1,1,2,2,2]
barcodes = [1,1,1,1,2,2,3,3]

Solution().rearrangeBarcodes(barcodes)