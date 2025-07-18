# heap - medium
import heapq
class Solution:
    def totalCost(self, costs, k, candidates) -> int:
        
        # important to realise that once our left & right minHeap has considered all elements,
        # we stop ingesting new elements, this is facilitated by checking l <= r
        n = len(costs)
        ans = 0 

        # we maintain two minHeaps
        leftHeap = costs[:candidates]
        rightHeap = costs[max(n - candidates, candidates):]

        # we maintain two pointers to access the to-be-ingested elements to either heap
        l,r = candidates, n - candidates - 1
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)

        while k > 0:

            if not rightHeap or (leftHeap and rightHeap and leftHeap[0] <= rightHeap[0]):
                ans += heapq.heappop(leftHeap)
                if l <= r:
                    heapq.heappush(leftHeap, costs[l])
                    l += 1
                    
            elif not leftHeap or (leftHeap and rightHeap and rightHeap[0] < leftHeap[0]):
                ans += heapq.heappop(rightHeap)
                if r >= l:
                    heapq.heappush(rightHeap, costs[r])
                    r -= 1
            k -= 1

        return ans
    
costs, k, candidates = [17,12,10,2,7,2,11,20,8], 3, 4
costs, k, candidates = [1,2,4,1], 3, 3

Solution().totalCost(costs, k, candidates)