# string - medium
from typing import List
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        # simplify indexing by removing the brackets first
        s = s[1:-1]

        n = len(s)
        # create different splits
        splits = []
        for i in range(1, n):
            splits.append((s[:i], s[i:]))

        def get_coords(numStr:str):

            # given a numeric string, generate all
            # possible coordinates, w/ the option to place a dot
            m = len(numStr)
            
            res = []
            # if numStr itself does not contain leading '0's
            if numStr[0] != '0' or (numStr[0] == '0' and len(numStr) == 1):
                res.append(numStr) # w/o dot

            for i in range(1, m):
                l, r = numStr[:i], numStr[i:]
                if (l[0] != '0' or (l[0] == '0' and len(l) == 1)) and r.rstrip('0') == r:
                    res.append(l + '.' + r)

            return res

        ans = []
        for p1, p2 in splits:
            l, r = get_coords(p1), get_coords(p2)
            if not l or not r:
                continue

            for x in l:
                for y in r:
                    ans.append('('+ x + ', ' + y + ')')

        return ans
    
s = "(123)"
s = "(0123)"
s = "(00011)"

Solution().ambiguousCoordinates(s)