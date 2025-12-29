# backtracking - medium
from collections import defaultdict
from typing import List
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        # first parse the allowed patterns: "BCC" -> "BC":["C"]
        pDict = defaultdict(list)
        for x in allowed:
            pDict[x[:2]].append(x[-1])

        # use a backtracking func to exhaust all possibilities of building
        def f(currSt: List[str], nextSt: List[str], i: int) -> bool:

            # finished building the pyramid (at the top)
            if len(currSt) == 1:
                return True
            
            # move up in level (to next stack)
            if i == len(currSt)-1:
                return f(nextSt, [], 0)
            
            # prune dfs based on invalid keys on curr. and next stack
            ckey = currSt[i] + currSt[i+1]
            if not pDict[ckey]:
                return False

            if len(nextSt) >= 2:
                nkey = nextSt[-2] + nextSt[-1]
                if not pDict[nkey]:
                    return False
            
            res = False
            for option in pDict[ckey]:
                nextSt.append(option)
                res = f(currSt, nextSt, i+1)
                if res:
                    break
                nextSt.pop() # backtrack

            return res

        return f(list(bottom), [], 0)

bottom, allowed = "BCD", ["BCC","CDE","CEA","FFF"]
bottom, allowed = "AAAA", ["AAB","AAC","BCD","BBE","DEF"]

Solution().pyramidTransition(bottom, allowed)