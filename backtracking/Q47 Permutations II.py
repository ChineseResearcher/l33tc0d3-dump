# backtracking - medium
from typing import List
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        # key ideas:
        # 1) duplicate are allowed in the given nums, for nums = [1,1,2],
        # choosing indices (0,1,2) and (1,0,2) will give the same seq. which need to be de-dup
        # 2) a good way to avoid such duplication is to build a counter instead,
        # and rely on the counter to build unique permutations
        ans = []

        freq = Counter(nums)
        def f(seq:List[int], freq:int) -> None:

            if len(seq) == n:
                ans.append(seq[:])
                return

            for x in freq:
                if freq[x] > 0:
                    freq[x] -= 1
                    seq.append(x)
                    _ = f(seq, freq)
                    freq[x] += 1
                    seq.pop()

        _ = f([], freq)
        return ans

nums = [1,1,2]
nums = [1,2,3]

Solution().permuteUnique(nums)