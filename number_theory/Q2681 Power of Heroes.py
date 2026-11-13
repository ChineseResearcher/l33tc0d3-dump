# number theory - hard
class Solution:
    def sumOfPower(self, nums: list[int]) -> int:

        n = len(nums)
        MOD = int(1e9 + 7)
        # key ideas:
        # 1) we first sort nums, so each element we process is conveniently the max of the group

        # 2) for every nums[i] after sorting, we append it to all groups that can be formed
        # from nums[:i], and we need to know the sum of all group minimum

        # 3) maintain the sum of all group minimums as a prefix sum, and is multiplied by 2
        # at each index, as the number of groups that can be formed using the same minimum
        # doubles per index away
        nums.sort()
        n0 = nums[0]

        minSum, ans = n0, n0 * pow(n0, 2, MOD)
        for i in range(1, n):
            x = nums[i]
            ans += (minSum + x) * pow(x, 2, MOD)
            ans %= MOD
            # update sum of group minimums
            minSum = (minSum * 2 + x) % MOD

        return ans % MOD

nums = [2,1,4]
nums = [2,4,6]
nums = [1,1,1]

Solution().sumOfPower(nums)