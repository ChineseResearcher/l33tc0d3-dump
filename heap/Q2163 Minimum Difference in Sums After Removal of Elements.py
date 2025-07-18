# heap - hard
from typing import List
import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        n = len(nums) // 3

        # init. two arrays, storing the min & max sum of subseq. of length n
        arr_min, arr_max = [0] * len(nums), [0] * len(nums)

        # the core idea to solve the problem is we need to:
        # 1) minimise the sum of first part
        # 2) maximise the sum of second part

        ## solve the min subseq. sum problem with forward iteration ##
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)

        subseq_sum = sum(nums[:n])
        arr_min[n-1] = subseq_sum

        # the maximum index of the first part after deleting n elements
        # would be 2*n - 1 in the original nums arr.
        r = 2 * n

        for i in range(n, r):

            subseq_sum += nums[i]
            heapq.heappush(max_heap, -nums[i])

            curr_max = heapq.heappop(max_heap)
            subseq_sum -= abs(curr_max)

            arr_min[i] = subseq_sum

        ## solve the max subseq. sum problem with backward iteration ##
        min_heap = [x for x in nums[-n:]]
        heapq.heapify(min_heap)

        subseq_sum = sum(nums[-n:])
        arr_max[-n] = subseq_sum

        # the minimum index of the second part after deleting n elements
        # would be n in the original nums arr.
        l = n-1

        for j in range(len(nums)-n-1, l, -1):

            subseq_sum += nums[j]
            heapq.heappush(min_heap, nums[j])

            curr_min = heapq.heappop(min_heap)
            subseq_sum -= curr_min

            arr_max[j] = subseq_sum

        # compute the final answer by scanning indices in range [n-1, len(nums)-n]
        ans = float('inf')
        for k in range(n-1, r):

            ans = min(ans, arr_min[k] - arr_max[k+1])

        return ans
    
nums = [3,1,2]
nums = [7,9,5,8,1,3]
nums = [1,3,100,2,4,5]

Solution().minimumDifference(nums)