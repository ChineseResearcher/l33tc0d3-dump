# counting - medium
class Solution:
    def countNicePairs(self, nums) -> int:
        n = len(nums)
        # a good pair is defined as nums[i] + reverse(nums[j]) == nums[j] + reverse(nums[i])
        # that equality is equivalent to nums[i] - reverse(nums[i]) == nums[j] - reverse(nums[j])

        # note that reverse(210) = 12, leading 0s all truncated
        diff_dict = dict()

        ans = 0
        for j in range(n):

            diff = nums[j] - int(str(nums[j])[::-1].lstrip('0')) if nums[j] != 0 else nums[j]
            if diff not in diff_dict:
                diff_dict[diff] = 1
                continue

            # if such a diff has been recorded before, increment ans by its count
            ans += diff_dict[diff]
            diff_dict[diff] += 1
            diff_dict[diff] %= 1e9 + 7

        return int(ans % (1e9 + 7))
    
nums = [42,11,1,97]
nums = [13,10,35,24,76]

Solution().countNicePairs(nums)