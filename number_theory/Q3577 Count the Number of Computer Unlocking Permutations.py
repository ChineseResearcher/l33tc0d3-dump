# number theory - medium
from typing import List
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        n = len(complexity)
        # because unlocking a computer i using computer j requires
        # (1) j < i and
        # (2) complexity[j] < complexity[i]
        # then it would be immediately impossible to unlock all 
        # if there's a computer i w/ complexity smaller than complexity[0] for i > 0
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        # if the above did not return 0, answer is simple (n-1)!
        # why? 
        # 1) we want permutations of computer indidce, not password complexities
        # 2) imagine if first computer can already unlock all remaining, then
        # we would just unlock all at one go, but in different orders. Exhausting all
        # orders possible would simply give us (n-1)!
        ans, MOD = 1, int(1e9 + 7)
        for i in range(n-1, 0, -1):
            ans *= i
            ans %= MOD

        return ans
    
complexity = [1,2,3]
complexity = [3,3,3,4,4,4]

Solution().countPermutations(complexity)