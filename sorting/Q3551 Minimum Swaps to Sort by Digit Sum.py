# sorting - medium
class Solution:
    def minSwaps(self, nums: list[int]) -> int:

        n = len(nums)
        # key ideas:
        # 1) sort all numbers by digit sum first, followed by number itself
        # 2) record the original indices of all (distinct) numbers for swapping
        # 3) mark an increment if nums[i] != sorted_nums[i]
        p = {x: i for i, x in enumerate(nums)}

        def ds(x: int) -> int:
            res = 0
            while x > 0:
                res += x % 10
                x //= 10
            return res

        sorted_nums = sorted(nums, key=lambda x: (ds(x), x))

        ans = 0
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                ans += 1
                # perform swap
                ni = p[sorted_nums[i]]
                nums[ni] = nums[i]
                # update index
                p[nums[i]] = ni 

        return ans

nums = [37,100]
nums = [22,14,33,7]
nums = [18,43,34,16]
nums = [625468152,191921893,821181574]

Solution().minSwaps(nums)