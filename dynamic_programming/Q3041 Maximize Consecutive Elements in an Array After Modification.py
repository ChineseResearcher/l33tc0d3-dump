# dp - hard
class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:

        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) variant of the classic LIS problem
        # 2) we do not care about original order since the final subsequence
        # will be sorted, so we can sort nums at the start
        # 3) build a hashtable where dp[i] refers to the longest length so far
        # with number i as the last element
        nums.sort()

        # unmodified
        dp_0 = {x: 1 for x in nums}
        # modified
        dp_1 = dict()

        # length is at least 1
        ans = 1
        for i in range(n):
            x = nums[i]

            v0 = 0
            # assume nums[i] is unchanged
            if x - 1 in dp_0:
                v0 = fmax(v0, 1 + dp_0[x - 1])
            if x - 1 in dp_1:
                v0 = fmax(v0, 1 + dp_1[x - 1])

            v1 = 0
            # modify nums[i]
            if x + 1 not in dp_1:
                dp_1[x + 1] = 1
            else:
                v1 = fmax(v1, 1 + dp_0[x])
            if x in dp_1:
                v1 = fmax(v1, 1 + dp_1[x])

            dp_0[x] = fmax(dp_0[x], v0)
            dp_1[x + 1] = fmax(dp_1[x + 1], v1)
            ans = fmax(ans, fmax(dp_0[x], dp_1[x + 1]))

        return ans

nums = [1,4,7,10]
nums = [2,1,5,1,1]
nums = [11,8,9,15,11,8,12,13,14]
nums = [8,10,6,12,9,12,2,3,13,19,11,18,10,16]

Solution().maxSelectedElements(nums)