# array - easy
class Solution:
    def isArraySpecial(self, nums) -> bool:
        n = len(nums)

        # one nice property about parity is that:
        # odd + even -> odd
        # odd + odd OR even + even -> even
        for i in range(1, n):
            if (nums[i] + nums[i-1]) % 2 == 0:
                return False

        return True
    
nums = [1]
nums = [2,1,4]
nums = [4,3,1,6]