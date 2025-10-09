# prefix sum - medium
from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        n, m = len(skill), len(mana)
        # core ideas:
        # 1) use prefix-sum to obtain the earliest start time possible
        # s.t. once the curr. potion is being brewed, there is no in-between waiting

        # 2) for every potion (mana arr.) build the cumulative 
        # finished timings for every wizard (skill arr.)
        doneBy = [0] * n

        # build a prefix sum on skill arr.
        skill_pf, cSum = [], 0
        for i in range(n):
            cSum += skill[i]
            skill_pf.append(cSum)

        for potion in mana:

            # init. the curr. round earliest start time to 
            # the start time of the previous round
            et = doneBy[0]

            for i in range(1, n):

                # create the timestamp that would satisfy up to
                # the i-th wizard with skill[i]
                ct = doneBy[i] - skill_pf[i-1] * potion

                # track worst
                if ct > et:
                    et = ct

            # re-write the doneBy arr. with the finished timings of the curr. potion
            doneBy[0] = et + skill[0] * potion
            for i in range(1, n):
                doneBy[i] = doneBy[i-1] + skill[i] * potion

        return doneBy[-1]
    
skill, mana = [1,5,2,4], [5,1,4,2]
skill, mana = [1,1,1], [1,1,1]
skill, mana = [1,2,3,4], [1,2]
# constraint
import random
skill, mana = [random.randint(1, 5000) for _ in range(5000)], [random.randint(1, 5000) for _ in range(5000)]

Solution().minTime(skill, mana)