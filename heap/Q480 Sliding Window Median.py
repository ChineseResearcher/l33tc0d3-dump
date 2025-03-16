# heap - hard
import heapq
class Solution:
    def medianSlidingWindow(self, nums, k):

        # edge case: if k = 1, means slided window is always of length 1
        if k == 1: return nums
        
        n = len(nums)
        # the idea is to have first half of the slided window be built
        # based on maxheap, and second half of the slided window be 
        # built based on minheap, taking into consideration of k being even/odd
        maxheap, minheap = [], []

        isEven = True if k % 2 == 0 else False
        for i in range(k):

            if not maxheap:
                heapq.heappush(maxheap, [-nums[i], i])
                continue

            if nums[i] <= -maxheap[0][0]:
                heapq.heappush(maxheap, [-nums[i], i])
            else:
                heapq.heappush(minheap, [nums[i], i])

            # balancing: always make sure maxheap.size() <= minheap.size() + 1
            if len(maxheap) > len(minheap) + 1:
                num, idx = heapq.heappop(maxheap)
                heapq.heappush(minheap, [-num, idx])

            elif len(minheap) > len(maxheap):
                num, idx = heapq.heappop(minheap)
                heapq.heappush(maxheap, [-num, idx])

        ans = [(-maxheap[0][0] + minheap[0][0]) / 2] if isEven else [-maxheap[0][0]] 

        l = 0
        for r in range(k, n):

            # our goal is to maintain the balanced state between max/min heap for all the
            # valid elements even though each heap might contain some number of invalid elements

            # there are only two cases that would trigger imbalance
            # 1) nums[l] (out-of-window) belongs to maxheap, and nums[r] (new-to-window)
            # belongs to minheap, so to balance pass one element from min. to max. heap

            # 2) nums[l] belongs to minheap, and nums[r] belongs to maxheap,
            # so to balance pass one element from max. to min heap

            if nums[r] <= -maxheap[0][0]:
                heapq.heappush(maxheap, [-nums[r], r])
                # imbalance case 2)
                # notice a detail that >= is enforced instead of >
                # this is because nums[l] can happen to be peak of maxheap
                if nums[l] >= -maxheap[0][0]:
                    num, idx = heapq.heappop(maxheap)
                    heapq.heappush(minheap, [-num, idx])

            else:
                heapq.heappush(minheap, [nums[r], r])
                # imbalance case 1)
                if nums[l] <= -maxheap[0][0]:
                    num, idx = heapq.heappop(minheap)
                    heapq.heappush(maxheap, [-num, idx])

            # lazy deletions on invalid elements
            while maxheap and maxheap[0][1] <= l:
                heapq.heappop(maxheap)

            while minheap and minheap[0][1] <= l:
                heapq.heappop(minheap)

            if isEven:
                ans.append((-maxheap[0][0] + minheap[0][0]) / 2)
            else:
                ans.append(-maxheap[0][0])

            l += 1  

        return ans
    
nums, k = [1,3,-1,-3,5,3,6,7], 3
nums, k = [1,2,3,4,2,3,1,4,2], 3
nums, k = [1,1,1,1], 2
nums, k = [1,2], 1

Solution().medianSlidingWindow(nums, k)