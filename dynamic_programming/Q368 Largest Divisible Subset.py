# dp - medium
class Solution:
    def largestDivisibleSubset(self, nums):
        # sorting the numbers makes it convenient for us to build inheritance
        # as nums[i] could inherit from the divisible set associated with nums[j]
        # if: 1) nums[i] % nums[j] = 0 and 2) nums[i] >= nums[j]
        # e.g. suppose the divisible set for nums[j] = 6 is {1,2,3,6} then for
        # some nums[i] = 18, it directly inherits the set
        nums.sort()
        n = len(nums)

        # each number is at least divisible by itself
        dp = [[x] for x in nums] 

        ans, maxLen = [nums[0]], 1
        for i in range(1, n):

            # we not only want to inherit from the smaller divisible
            # number, we want to inherit from the one with the largest set
            currBest = None
            for j in range(i):
                if nums[i] % nums[j] == 0:

                    if currBest is None:
                        currBest = j
                    else:
                        if len(dp[j]) > len(dp[currBest]):
                            currBest = j

            if currBest is not None:
                dp[i].extend(dp[currBest])

            # track best answer
            if len(dp[i]) > maxLen:
                ans = dp[i]
                maxLen = len(dp[i])

        return ans
    
nums = [1,2,3]
nums = [1,2,4,8]
nums = [5,9,18,54,108,540,90,180,360,720]

Solution().largestDivisibleSubset(nums)