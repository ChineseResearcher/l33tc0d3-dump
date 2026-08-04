# backtracking - medium
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        # key ideas:
        # 1) given nums.length <= 6, use a bitmask to track used indices
        # 2) permute all sequences using backtracking 

        ans = []

        def f(seq:List[int], mask:int) -> None:

            nonlocal ans
            if len(seq) == n:
                ans.append(seq[:])
                return

            for i in range(n):
                p = (1 << i)
                if not mask & p:
                    mask |= p
                    seq.append(nums[i])
                    _ = f(seq, mask)
                    mask &= ~p # backtrack
                    seq.pop()

        _ = f([], 0)
        return ans

nums = [1]
nums = [0,1]
nums = [1,2,3]

Solution().permute(nums)