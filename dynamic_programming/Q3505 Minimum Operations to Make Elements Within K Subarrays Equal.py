# dp - hard
from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:

        n = len(nums)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) use ordered sets to pre-compute the median and associated moves required
        # 2) iterative DP to build the optimal moves towards k non-overlapping selections
        # 3) ops[i] denotes the optimal number of operations to make subarray nums[i-x+1:i] equal
        # by choosing median of the subarray to be the convergence target
        left, right = SortedList(), SortedList()

        sum_l, sum_r, ops = 0, 0, [0] * n
        for i, value in enumerate(nums):
            # manage new element
            if not left or value <= left[-1]:
                left.add(value)
                sum_l += value
            else:
                right.add(value)
                sum_r += value
            # manage expired element
            if i >= x:
                value = nums[i - x]
                if value in left:
                    left.remove(value)
                    sum_l -= value
                else:
                    right.remove(value)
                    sum_r -= value
            # balance length of 2 ordered sets
            # note: it is balanced when right.length <= left.length <= right.length + 1
            if len(left) > len(right) + 1:
                value = left.pop()
                right.add(value)
                sum_l -= value
                sum_r += value
            elif len(left) < len(right):
                value = right.pop(0)
                left.add(value)
                sum_l += value
                sum_r -= value
            # for subarrays meeting length = x, we can pre-compute the ops
            # arising from choosing the median as the target to converge to
            if i >= x - 1:
                mid = left[-1]
                ops[i] = mid * len(left) - sum_l + sum_r - mid * len(right)

        dp = [ [float('inf')] * (n + 1) for _ in range(k + 1) ]
        for i in range(n + 1):
            dp[0][i] = 0

        for i in range(x, n + 1):
            for j in range(1, k + 1):
                dp[j][i] = fmin(dp[j][i - 1], dp[j - 1][i - x] + ops[i - 1])

        return dp[k][n]

nums, x, k = [9,-2,-2,-2,1,5], 2, 2
nums, x, k = [5,-2,1,3,7,3,6,4,-1], 3, 2

Solution().minOperations(nums, x, k)