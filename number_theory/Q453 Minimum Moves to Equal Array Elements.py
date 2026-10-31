# number theory - medium
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) math observation: incrementing all except 1 is equivalent
        # to reducing that 1 number by 1
        # 2) the cheapest way to reduce is just to reduce the min(nums)
        
        m, s = float('inf'), 0
        for x in nums:
            m = fmin(m, x)
            s += x

        return s - len(nums) * m

nums = [1,1,1]
nums = [1,2,3]
nums = [1,3,4,6]

Solution().minMoves(nums)