# backtracking - easy
from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        def backtrack(chosen: List[int], options: List[int], currIdx: int, target: int) -> set:

            if currIdx >= len(options) or len(chosen) == target:

                if currIdx >= len(options) and len(chosen) < target:
                    return set()
                    
                # if options is "hour" then we cannot exceed 11
                if len(options) == 4:
                    limit = 11
                # otherwise the limit for "minutes" is 59
                else:
                    limit = 59

                chosen_sum = sum(chosen)
                if chosen_sum <= limit:
                    return {chosen_sum}

            res = set()
            for i in range(currIdx, len(options)):

                chosen.append(options[i])
                next_res = backtrack(chosen, options, i+1, target)
                res |= next_res
                chosen.pop()

            return res

        hours = [8,4,2,1]
        minutes = [32,16,8,4,2,1]

        # pre-compute all possible formations for all targets
        h_choice = dict()
        for target in range(0, 4):
            h_choice[target] = backtrack([], hours, 0, target)

        m_choice = dict()
        for target in range(0, 6):
            m_choice[target] = backtrack([], minutes, 0, target)

        # find all valid combinations given turnedOn
        ans = set()
        for hour_cnt in range(turnedOn + 1):

            minute_cnt = turnedOn - hour_cnt
            # invalid splits
            if hour_cnt >= 4 or minute_cnt >= 6:
                continue

            for h in h_choice[hour_cnt]:
                for m in m_choice[minute_cnt]:
                    ans.add(str(h) + ":" + f"{m:02}")

        return sorted(list(ans))

turnedOn = 2
turnedOn = 10

Solution().readBinaryWatch(turnedOn)