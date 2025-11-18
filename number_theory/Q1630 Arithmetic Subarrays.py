# number theory - medium
from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        # key ideas:
        # 1) O(n^2) soln with inner loop determining if a range [l,r] is valid
        # 2) for k elements with k-1 gaps, the diff between MAX and MIN
        # must be divisible by (k-1), if satisfied we have to further check
        # if every [MIN+u, MIN+2*u, ..., MAX] is present in range
        m = len(l)

        ans = []
        for i in range(m):
            lb, rb = l[i], r[i]

            numSet, rangeMin, rangeMax = set(), float('inf'), float('-inf')
            for j in range(lb, rb+1):
                numSet.add(nums[j])

                # range MIN / MAX update
                if nums[j] > rangeMax:
                    rangeMax = nums[j]
                if nums[j] < rangeMin:
                    rangeMin = nums[j]

            gaps, interval = rb - lb, rangeMax - rangeMin
            if interval == 0:
                ans.append(True)
                continue

            if interval % gaps != 0:
                ans.append(False)
                continue

            # step size
            u = interval // gaps

            res = True
            for num in range(rangeMin, rangeMax+1, u):
                if num not in numSet:
                    res = False
                    break

            ans.append(res)

        return ans

nums, l, r = [4,6,5,9,3,7], [0,0,2], [2,3,5]
nums, l, r = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]
nums, l, r = [-3,-6,-8,-4,-2,-8,-6,0,0,0,0], [5,4,3,2,4,7,6,1,7], [6,5,6,3,7,10,7,4,10]

Solution().checkArithmeticSubarrays(nums, l, r)