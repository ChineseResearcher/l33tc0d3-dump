# dp - hard
from typing import List
from functools import cache
class Solution:
    def canCross(self, stones: List[int]) -> bool: 

        if stones[1] != 1:
            return False

        if len(stones) == 2:
            return True

        target = stones[-1]
        stones = set(stones)

        @cache
        def recursive_jump(pos, prevJumpR):

            if pos == target:
                return True
            
            curr_ans = False
            for choice in [prevJumpR-1, prevJumpR, prevJumpR+1]:
                new_pos = pos + choice

                if new_pos > pos and new_pos in stones:
                    curr_ans = (curr_ans or recursive_jump(new_pos, choice))

            return curr_ans

        return recursive_jump(1, 1)
    
stones = [0,1,3,5,6,8,12,17]
stones = [0,1,2,3,4,8,9,11]

Solution().canCross(stones)