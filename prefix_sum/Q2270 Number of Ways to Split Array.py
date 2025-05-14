# prefix sum - medium
class Solution:
    def waysToSplitArray(self, nums):
        n = len(nums)
        pf_sum = []

        curr_sum = 0
        for num in nums:
            curr_sum += num
            pf_sum.append(curr_sum)

        ans = 0
        # for valid splits, partition must not be empty
        for i in range(n-1):
            if pf_sum[i] >= pf_sum[-1] - pf_sum[i]:
                ans += 1

        return ans
    
nums = [10,4,-8,7]
nums = [2,3,1,0]

Solution().waysToSplitArray(nums)