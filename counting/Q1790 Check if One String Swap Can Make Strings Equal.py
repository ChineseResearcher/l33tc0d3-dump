# counting - easy
from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # not possible to get equal strings if they are made up of different alphabets
        if Counter(s1) != Counter(s2):
            return False

        n = len(s1)
        # if two strings differ at more than 2 positions, not possible to swap once
        diff_cnt = 0
        for i in range(n):

            if s1[i] != s2[i]: diff_cnt += 1
            if diff_cnt > 2: 
                return False

        return True
    
s1, s2 = "bank", "kanb"
s1, s2 = "abcd", "dcba"
s1, s2 = "rywib", "bywir"
s1, s2 = "gemvejmohpmkg", "hemvejmogpmkg"

Solution().areAlmostEqual(s1, s2)