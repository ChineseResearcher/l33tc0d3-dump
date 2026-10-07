# dp - hard
import bisect
from functools import cache
class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:

        m, n = len(arr1), len(arr2)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) DP + binary search on sorted arr2
        # 2) for every arr1[i], we either keep it or find the smallest greater
        # element from arr2 s.t. arr2[j] > (possibly replaced) value at arr1[i - 1] (i.e. prev)
        arr2.sort()

        # helper to return smallest greater element in arr2
        def gt(x: int) -> int:
            j = bisect.bisect_right(arr2, x)
            return arr2[j] if j < n else float('inf')

        @cache
        def f(i: int, prev: int) -> int:

            if i == m:
                return 0

            res = float('inf')
            # do not replace (cond. on strictly greater)
            if arr1[i] > prev:
                res = fmin(res, f(i + 1, arr1[i]))

            # if we can find a valid replacement, try replacing
            sg = gt(prev)
            if sg < float('inf'):
                res = fmin(res, 1 + f(i + 1, sg))

            return res

        res = f(0, -1)
        return res if res < float('inf') else -1

arr1, arr2 = [1,5,3,6,7], [4,3,1]
arr1, arr2 = [1,5,3,6,7], [1,3,2,4]
arr1, arr2 = [1,5,3,6,7], [1,6,3,3]
arr1, arr2 = [0,11,6,1,4,3], [5,4,11,10,1,0]

Solution().makeArrayIncreasing(arr1, arr2)