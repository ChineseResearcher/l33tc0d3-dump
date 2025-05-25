# heap - hard
from typing import List
import heapq
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        m, n = len(flowers), len(people)
        # sort both flowers & people arrays to make heap operations possible
        ans = [0] * n

        flowers.sort()
        people = sorted([(people[i], i) for i in range(n)])

        minheap = []
        # maintain a pointer to access flowers
        j = 0

        for t, idx in people:

            while j < m and flowers[j][0] <= t:
                heapq.heappush(minheap, flowers[j][1])
                j += 1

            while minheap and t > minheap[0]:
                heapq.heappop(minheap) 

            ans[idx] = len(minheap)

        return ans
    
flowers, people = [[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]
flowers, people = [[1,10],[3,3]], [3,3,2]

Solution().fullBloomFlowers(flowers, people)