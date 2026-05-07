# dp - medium
from typing import List
from functools import cache
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:

        n = len(nums)
        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) for any arr[i], the max. reachable value comes from:
        # either arr[0...i-1] or arr[i+1...j] where j is the index
        # of the rightmost smaller element w.r.t to arr[i]

        # 2) build prefixMax and suffixMin arrays, and use binary search
        # on suffixMin array in the range [i+1, n-1] for each arr[i]
        # so as to obtain the potentially max. element in arr[i+1...j]

        prefixMax = [float('-inf')] * n
        prefixMax[0] = nums[0]

        prefixMaxIdx = dict()

        for i in range(1, n):
            if nums[i] > prefixMax[i-1]:
                prefixMax[i] = nums[i]
                prefixMaxIdx[prefixMax[i]] = i
            else:
                prefixMax[i] = prefixMax[i-1]

        suffixMin = [float('inf')] * n
        suffixMin[-1] = nums[-1]

        for i in range(n-2, -1, -1):
            suffixMin[i] = fmin(suffixMin[i+1], nums[i])

        @cache
        def f(i: int) -> int:

            res = prefixMax[i]
            # perform binary search on [i+1, n-1] on the suffixMin arr.
            l, r = i+1, n-1

            ri = i
            while l <= r:

                mid = (l + r) // 2
                if suffixMin[mid] < res:
                    l = mid + 1
                    ri = fmax(ri, mid)
                else:
                    r = mid - 1

            if prefixMax[ri] > res:
                return f(prefixMaxIdx[prefixMax[ri]])
            
            return res

        ans = []
        for i in range(n):
            ans.append(f(i))

        return ans

nums = [2,1,3]
nums = [2,3,1]
nums = [30,21,5,35,24]
nums = [9,30,16,6,36,9]

Solution().maxValue(nums)