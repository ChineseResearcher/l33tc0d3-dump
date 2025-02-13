# heap - medium
import heapq
class Solution:
    def minOperations(self, nums, k):
        # first heapify nums to be a min heap
        heapq.heapify(nums)

        ans = 0
        # always pop the two smallest element and perform op
        while True:

            if nums[0] >= k: break

            s1, s2 = heapq.heappop(nums), heapq.heappop(nums)
            # add the manipulated number
            heapq.heappush(nums, min(s1, s2) * 2 + max(s1, s2))

            ans += 1

        return ans
    
nums, k = [2,11,10,1,3], 10
nums, k = [1,1,2,4,9], 20

Solution().minOperations(nums, k)