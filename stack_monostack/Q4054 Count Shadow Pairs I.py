# monotonic stack - medium
from functools import cache
class Solution:
    def shadowPairs(self, nums: list[int]) -> int:

        n = len(nums)
        # key ideas:
        # 1) build a array to store the prevSmaller elements using monotonic stack
        # 2) perform a DP search to compute array "c" where c[i] stores the length
        # of the longest non-ascending array starting from index i going backwards

        prevSmaller, st = [-1] * n, []
        for i in range(n - 1, -1, -1):
            while st and nums[i] <= nums[st[-1]]:
                prevSmaller[st.pop()] = i
            st.append(i)

        @cache
        def L(i: int) -> int:
            if i == -1: return 0
            return 1 + L(prevSmaller[i])

        c = [0]* n
        for i in range(n - 1, -1, -1):
            c[i] = L(i)

        ans, v = 0, set()
        for i in range(n - 1, -1, -1):
            if i in v: continue

            v.add(i)
            # dupCnt tracks the count of nums[i] as we iterate prevSmaller
            dupCnt, j = 1, i
            while prevSmaller[j] >= 0 and nums[prevSmaller[j]] == nums[j]:
                j = prevSmaller[j]
                v.add(j)
                dupCnt += 1
            ans += dupCnt * (c[i] - dupCnt)

        return ans

nums = [1,2,3,4]
nums = [3,1,4,1,5]
nums = [6,7,6,6,7]
nums = [17,22,35,33,27,10]

Solution().shadowPairs(nums)