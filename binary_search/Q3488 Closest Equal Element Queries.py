# binary search - medium
import bisect
from typing import List
from collections import defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        m, n = len(nums), len(queries)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) store indices of unique numbers in hashmap
        # 2) use binary search to locate its position in the indice list
        # and compare with left/right neighbours

        pos = defaultdict(list)
        for i in range(m):
            pos[nums[i]].append(i)

        # helper to get min. dist between two indices
        def min_dist(u:int, v:int) -> int:
            if u > v:
                u, v = v, u
            return fmin(u + m - v, v - u)

        ans = []
        for q in queries:

            arr = pos[nums[q]]
            k = len(arr)

            if k == 1:
                ans.append(-1)
                continue

            curr = float('inf')

            qi = bisect.bisect_left(arr, q)
            # compare w/ left neighbour
            L = (qi - 1 + k) % k
            curr = fmin(curr, min_dist(arr[L], q))

            # compare w/ right neighbour
            R = (qi + 1 + k) % k
            curr = fmin(curr, min_dist(arr[R], q))

            ans.append(curr)

        return ans

nums, queries = [1,2,3,4], [0,1,2,3]
nums, queries = [1,3,1,4,1,3,2], [0,3,5]

Solution().solveQueries(nums, queries)