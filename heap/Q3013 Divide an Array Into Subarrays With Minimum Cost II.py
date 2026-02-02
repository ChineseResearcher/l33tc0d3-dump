# heap - hard
import heapq
from typing import List
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:

        n = len(nums)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) To build k contiguous disjoint intervals, we need to have k-1
        # indices in the range [1, n-1], and thus for every nums[i] s.t. i > 0
        # we find the sum of smallest k-2 elements in the range [i+1, i+dist]

        # 2) Use a minheap to query for the next best element to qualify for the
        # curr. smallest k-2 elements, and as we are sliding a fixed window,
        # maintain a hashset of indices that indicate the currently active k-2 elements

        # 3) We use a maxheap to store the active k-2 elements, and possibly
        # replace w/ the curr. best minheap[0] if maxheap[0] > minheap[0]
        minheap, maxheap = [], []
        for i in range(2, min(1+dist+1, n)):
            heapq.heappush(minheap, (nums[i], i)) # <val, idx>

        # currSum tracks the sum of k-2 elements
        active, currSum, ans = set(), 0, float('inf')
        for i in range(1, n):

            while minheap and len(active) < k-2:
                val, idx = heapq.heappop(minheap)
                # expired pair
                if idx <= i:
                    continue

                active.add(idx)
                heapq.heappush(maxheap, (-val, idx))
                currSum += val

            # curr. active set cannot recruit k-2 elements, early terminate
            if len(active) < k-2:
                break

            # replacement
            while maxheap and minheap:
                # expired pair
                if maxheap[0][1] <= i:
                    heapq.heappop(maxheap)
                    continue
                if minheap[0][1] <= i:
                    heapq.heappop(minheap)
                    continue

                # compare
                if -maxheap[0][0] > minheap[0][0]:
                    val, idx = heapq.heappop(maxheap)
                    active.discard(idx)
                    currSum -= -val
                    heapq.heappush(minheap, (-val, idx)) # re-push the pair into minheap
                    val, idx = heapq.heappop(minheap)
                    heapq.heappush(maxheap, (-val, idx))
                    active.add(idx)
                    currSum += val
                else:
                    break

            ans = fmin(ans, nums[0] + nums[i] + currSum)
            
            # slide window to obtain new element and also discard
            # nums[i+1] if it is in active
            r = i + 1 + dist
            if r < n:
                heapq.heappush(minheap, (nums[r], r))
            if i + 1 in active:
                active.discard(i+1)
                currSum -= nums[i+1]

        return ans
    
nums, k, dist = [1,3,2,6,4,2], 3, 3
nums, k, dist = [10,1,2,2,2,1], 4, 3
nums, k, dist = [10,8,18,9], 3, 1
nums, k, dist = [6,40,41,11,50,15,47,48,50,12,16,30,38,45,13,34,26,25,32,28], 9, 13
nums, k, dist = [34,37,38,6,10,30,42,43,33,2,2,24,44,40,47,5,44,28,16,32,25,9,30,49,12,31,42,35,12,25], 18, 27

Solution().minimumCost(nums, k, dist)