# heap - hard
from typing import List
import heapq
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        # we sort the numbers in ASC order but using absolute vals
        # this allows us to always access the next smallest +ve / largest -ve number
        nums.sort(key = lambda x: abs(x))

        # the first (largest sum) is the sum of all non-negative numbers
        maxSum = sum([x for x in nums if x >= 0]) # init. to 0 if all -ve

        # perform a tree-like traversal through all unique
        # combinations (subseq.) greedily w/ the use of priority queue
        res, maxHeap = [maxSum], [[-(maxSum - abs(nums[0])), 1]] # <next largest subseq. sum, idx>

        while maxHeap:

            if len(res) == k:
                break

            # curr. largest
            curr, idx = heapq.heappop(maxHeap)
            curr = -curr # invert
            res.append(curr)

            if idx < n:

                # we are dealing w/ abs number including negative numbers
                # because adding -ve numbers to decrease the curr. sum is equivalent
                # to subtracting the abs. val of the -ve number

                # op1: keep previous decision
                op1 = curr - abs(nums[idx])

                # op2: invert previous (pick) decision
                op2 = curr + abs(nums[idx-1]) - abs(nums[idx])

                # note: we are always picking the curr. element
                # as the element to be subtracted to obtain the next smaller subseq. sum
                heapq.heappush(maxHeap, [-op1, idx+1])
                heapq.heappush(maxHeap, [-op2, idx+1])

        return res[-1]
    
nums, k = [2,4,-2], 5
nums, k = [1,-2,3,4,-10,12], 16

Solution().kSum(nums, k)