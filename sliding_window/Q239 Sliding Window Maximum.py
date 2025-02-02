import heapq
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        
        n = len(nums)

        # idea is to create a max-heap storing <-num, num idx>
        # and the max. num is validated if num idx is greater than curr. left pointer
        max_heap = []

        # first initiate k elements
        for i in range(k):
            heapq.heappush(max_heap, [-nums[i], i])

        ans = [-max_heap[0][0]]
        for i in range(k, n):

            # ingest new element
            heapq.heappush(max_heap, [-nums[i], i])

            # discard invalid max. val
            while max_heap[0][1] <= i-k:
                heapq.heappop(max_heap)

            ans.append(-max_heap[0][0])

        return ans
    
nums, k = [1,3,-1,-3,5,3,6,7], 3
nums, k = [1], 1

Solution().maxSlidingWindow(nums, k)