# simulation - medium
from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)
        MOD = int(1e9 + 7)
        for l, r, k, v in queries:
            for i in range(l, r+1, k):
                nums[i] = (nums[i] * v) % MOD

        XOR = 0
        for x in nums:
            XOR ^= x

        return XOR

nums, queries = [1,1,1], [[0,2,1,4]]
nums, queries = [2,3,1,5,4], [[1,4,2,3],[0,2,1,2]]

Solution().xorAfterQueries(nums, queries)