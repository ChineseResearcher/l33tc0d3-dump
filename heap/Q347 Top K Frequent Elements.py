# heap - medium
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k):

        num_freq = Counter(nums)

        # initiate a max_heap storing <freq, num>
        max_heap = [[-v, k] for k,v in num_freq.items()]
        heapq.heapify(max_heap)

        ans = []
        while k > 0:

            ans.append(max_heap[0][1])
            heapq.heappop(max_heap)

            k -= 1

        return ans
    
nums, k = [1,1,1,2,2,3], 2

Solution().topKFrequent(nums, k)