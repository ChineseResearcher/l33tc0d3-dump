# binary search - medium
from typing import List
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # core idea:
        # 1) first construct a prefix sum of bit counts w/ 30 x n in dimensions
        # 2) compute max. bitwise OR possible for each nums[i...n-1] for i in range [0, n-1]
        # 3) iterate i from left to right, and compute the shortest subarr. using prefix sum
        # table from (1) and binary search

        bitCnt = [ [0] * n for _ in range(30) ]
        currCnt = [0] * 30
        for i in range(n):
            # nums[i] is at most 1e9
            for bitPos in range(30):
                if nums[i] & (1 << bitPos) != 0:
                    currCnt[bitPos] += 1
                bitCnt[bitPos][i] = currCnt[bitPos]

        # iterate backwards once to compute the max. bitwise OR for each index 
        maxOR, currOR = [0] * n, 0
        for i in range(n-1, -1, -1):
            currOR |= nums[i]
            maxOR[i] = currOR

        def bs(startIdx, bitIdx):

            l, r = startIdx, n-1
            prevCnt = bitCnt[bitIdx][startIdx-1] if startIdx > 0 else 0

            while l <= r:

                mid = (l + r) // 2
                if bitCnt[bitIdx][mid] - prevCnt > 0:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        # initiate ans. arr
        ans = [1] * n
        for i in range(n):

            # query for the min. rightmost pointer
            j = i
            for bitPos in range(30):
                if maxOR[i] & (1 << bitPos) != 0:
                    j = max(j, bs(i, bitPos))
            ans[i] = max(ans[i], j-i+1)

        return ans
    
nums = [1,0,2,1,3]
nums = [2,4,8,0,3]
nums = [1,2]

Solution().smallestSubarrays(nums)