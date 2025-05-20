# prefix sum - medium
from typing import List
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # build a diff arr of length n
        diff = [0] * n

        # process the queries such that the l indice marks diff[l] with +1
        # and that the r indice marks diff[r+1] with -1
        for l, r in queries:

            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1

        # to understand what diff[i] means, imagine we keep track of 
        # a variable that records how many times the current index i would be
        # involved in a query range, and this is also the criterion for us
        # to determine if nums[i] can be reduced to 0

        involvedCnt = 0
        for i in range(n):

            involvedCnt += diff[i]
            if involvedCnt < nums[i]:
                return False

        return True
    
nums, queries = [1,0,1], [[0,2]]
nums, queries = [4,3,2,1], [[1,3],[0,2]]
nums, queries = [0,0,1,2,1], [[2,4],[3,3]]

Solution().isZeroArray(nums, queries)