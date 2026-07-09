# graph - medium
import bisect
from typing import List
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        # key ideas:
        # 1) given an non-descending nums array, use binary search to find
        # the furthesta node to the right that would be able to form an edge
        # with the curr. unexplored node

        # 2) use the idea of "union-find" to mark all nodes in range [i..j]
        # to the same parent, where nums[j] is the rightmost node s.t. 
        # nums[j] - nums[i] <= maxDiff
        p = [i for i in range(n)]

        i = 0
        while i < n:

            parent = p[i]
            j = bisect.bisect_right(nums, nums[i] + maxDiff) - 1
            for k in range(i, j+1):
                p[k] = parent
            i = j if j > i else j + 1

        ans = []
        for a, b in queries:
            ans.append(p[a] == p[b])

        return ans

n, nums, maxDiff, queries = 2, [1,3], 1, [[0,0],[0,1]]
n, nums, maxDiff, queries = 4, [2,5,6,8], 2, [[0,1],[0,2],[1,3],[2,3]]

Solution().pathExistenceQueries(n, nums, maxDiff, queries)