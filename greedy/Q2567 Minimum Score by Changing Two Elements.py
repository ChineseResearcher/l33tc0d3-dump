# greedy - medium
class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) first sort nums to allow greedy to take place
        # 2) the low score can always be minimised to 0 by having 2 equal numbers
        # 3) the high score can be minimised the following ways:
        # - remove smallest 2, and achieve max(nums) - nums[2]
        # - remove largest 2, and achieve nums[-3] - min(nums)
        # - remove 1st and last, and achieve nums[-2] - nums[1]
        nums.sort()
        return fmin(nums[-1] - nums[2],
                    fmin(nums[-3] - nums[0],
                         nums[-2] - nums[1])
                         )

nums = [1,4,3]
nums = [1,4,7,8,5]
nums = [59,27,9,81,33]
nums = [58,42,8,75,28]

Solution().minimizeSum(nums)