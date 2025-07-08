# heap - medium
from typing import List
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    
        n = len(arr)
        # construct a minheap storing <frac_val, i, j> where i < j
        # we enqueue all fractions arr[0] / arr[j] for j in [1, n-1]
        minheap = []
        for j in range(1, n):
            heapq.heappush(minheap, [arr[0] / arr[j], 0, j])

        while k > 0:

            frac_val, i, j = heapq.heappop(minheap)
            k -= 1

            # otherwise we construct the next bigger fraction by shifting i
            # why don't we consider the other two options:
            # (arr[i] / arr[j-1]) & (arr[i+1] / arr[j-1]) ?
            # because by enqueuing all (arr[0] / arr[j]) for j in range [1, n-1] above
            # we would be able to cover the entire search space just by
            # considering (arr[i+1] / arr[j]) as the next bigger fraction each time
            if i < j - 1:
                heapq.heappush(minheap, [arr[i+1] / arr[j], i+1, j])

        return [arr[i], arr[j]]
    
arr, k = [1,2,3,5], 6
arr, k = [1,7,23,29,47], 8

Solution().kthSmallestPrimeFraction(arr, k)