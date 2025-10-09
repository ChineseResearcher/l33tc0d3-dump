# string - hard
from typing import List
from collections import defaultdict
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        
        n, m = len(s), len(sub)

        map = defaultdict(set)
        # create dict for mappings
        for u, v in mappings:
            map[u].add(v)

        # double-loop to see if "sub" can be a subtring
        # when substitutions are being made to the best extent
        for i in range(n-m+1):
            
            canMatch = True
            for j in range(m):

                if s[i+j] == sub[j]:
                    continue

                # otherwise, try to find a substitute
                if s[i+j] not in map[sub[j]]:
                    canMatch = False
                    break 

            if canMatch:
                break

        return canMatch
    
s, sub, mappings = "fool3e7bar", "leet", [["e","3"],["t","7"],["t","8"]]
s, sub, mappings = "fooleetbar", "f00l", [["o","0"]]
s, sub, mappings = "Fool33tbaR", "leetd", [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]

Solution().matchReplacement(s, sub, mappings)