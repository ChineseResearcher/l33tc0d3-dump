# bit manipulation - medium
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        
        # key ideas:
        # 1) determine all the numbers that are not in their correct positions
        # 2) the common bitwise AND of all numbers collected in (1) is the max. k
        # due to the fact that each misplaced has to be involved in at least 1 swap
        
        ans = None
        for i, x in enumerate(nums):
            if x != i:
                if ans is None:
                    ans = x
                else:
                    ans &= x
            
        return ans if ans is not None else 0

nums = [0,3,2,1]
nums = [0,1,3,2]
nums = [3,2,1,0]
nums = [0,2,3,1]

Solution().sortPermutation(nums)