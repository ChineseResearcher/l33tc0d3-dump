# heap - medium
import heapq
from typing import List
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        nums1, nums2 = zip(*sorted(zip(nums1, nums2)))

        n = len(nums1)
        idx, minheap, heapsum, score = -1, [], 0, 0

        while True:

            if abs(idx) > n:
                break
            
            while len(minheap) < k:
                heapq.heappush(minheap, [nums2[idx], nums1[idx]])
                heapsum += nums1[idx]
                idx -= 1

            score = max(score, minheap[0][0] * heapsum)
            heapsum -= minheap[0][1]
            heapq.heappop(minheap)

        return score

nums1, nums2, k = [1,3,3,2], [2,1,3,4], 3
nums1, nums2, k = [4,2,3,1,1], [7,5,10,9,6], 1

Solution().maxScore(nums1, nums2, k)