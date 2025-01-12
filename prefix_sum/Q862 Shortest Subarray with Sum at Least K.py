# prefix sum - hard
import heapq
class Solution:
    def shortestSubarray(self, nums, k):
        # general idea is to construct a minheap which stores <prefix sum at index i, i>
        # and as we iterate, check if window sum given by pfSum[idx] - smallest pfSum in minheap
        # would satisfy k, and greedily pop from minheap to see if we can achieve smaller subarr.

        n = len(nums)

        # any element >= k would mean that we only need subarray of size 1
        if max(nums) >=k: return 1

        n = len(nums)
        pfSum, currSum = [], 0
        for num in nums:
            currSum += num
            pfSum.append(currSum)

        ans = float('inf')
        minheap = [[0, -1]]

        for idx in range(n):

            # update minheap
            heapq.heappush(minheap, [pfSum[idx], idx])

            while pfSum[idx] - minheap[0][0] >= k:
                ans = min(ans, idx-minheap[0][1])
                heapq.heappop(minheap)

        return ans if ans < float('inf') else -1 
    
nums, k = [1], 1
nums, k = [1,2], 4
nums, k = [2,-1,2], 3
nums, k = [17,85,93,-45,-21], 150
nums, k = [84,-37,32,40,95], 167
nums, k = [56,-21,56,35,-9], 61
nums, k = [84,10,-37,20,-57,32,40,95], 167
nums, k = [-28,81,-20,28,-29], 89
nums, k = [-36,10,-28,-42,17,83,87,79,51,-26,33,53,63,61,76,34,57,68,1,-30], 484

Solution().shortestSubarray(nums, k)