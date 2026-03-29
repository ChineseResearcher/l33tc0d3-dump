# string - medium
from typing import List
from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        # key ideas:
        # 1) since we are free to exchange the positions of any letters
        # as long as they are even distances apart in original string (s1),
        # then we could replicate s2 as long as they have the same set of 
        # letters and their frequencies match

        # 2) read in s1, s2 at odd & even indices separately, and perform
        # a counter on both subsequences, and test if they match exactly

        def match(s1:List[str], s2:List[str]) -> bool:
            return Counter(s1) == Counter(s2)

        o_s1 = [s1[i] for i in range(1, n, 2)]
        o_s2 = [s2[i] for i in range(1, n, 2)]
        if not match(o_s1, o_s2):
            return False

        e_s1 = [s1[i] for i in range(0, n, 2)]
        e_s2 = [s2[i] for i in range(0, n, 2)]
        if not match(e_s1, e_s2):
            return False

        return True

s1, s2 = "abe", "bea"
s1, s2 = "abcdba", "cabdab"

Solution().checkStrings(s1, s2)