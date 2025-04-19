# two pointers - medium
class Solution:
    def countFairPairs(self, nums, lower, upper):
        n = len(nums)
        # the questions defines a fair pair (i, j) as 
        # 1) i < j
        # 2) lower <= nums[i] + nums[j] <= upper
        # But it DOESN'T restrict nums[i] to be < nums[j]
        nums.sort()

        # we can break down the problem into the sub-problems
        # CountPairSum <= lower-1 & CountPairSum <= upper
        def countPairSumSE(nums, target):

            l, r = 0, len(nums)-1

            cnt = 0
            # enforce a pair (i,j) so l, r cannot overlap
            while l < r:

                # keep shrinking pointer r until cond. fulfilled
                while l < r and nums[r] + nums[l] > target:
                    r -= 1

                cnt += r - l
                l += 1

            return cnt

        return countPairSumSE(nums, upper) - countPairSumSE(nums, lower-1)
    
nums, lower, upper = [0,1,7,4,4,5], 3, 6
nums, lower, upper = [1,7,9,2,5], 11, 11
nums, lower, upper = [-3,-2,0,2,3], -1, 1
nums, lower, upper = [6,9,4,2,7,5,10,3], 13, 13

Solution().countFairPairs(nums, lower, upper)