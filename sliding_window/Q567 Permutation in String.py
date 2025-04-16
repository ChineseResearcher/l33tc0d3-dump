# sliding window - medium
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for a window of fixed length equal to string s1
        # check if the set of chars of such a window in s2 matches s1

        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        s1_dict, s2_dict = Counter(s1), Counter(s2[:n1])
        if s1_dict == s2_dict:
            return True

        l = 0
        for r in range(n1, n2):
            
            left_char, right_char = s2[l], s2[r]
            
            # left end
            s2_dict[left_char] -= 1
            if s2_dict[left_char] == 0:
                del s2_dict[left_char]     
            l += 1
                
            # right end
            if right_char in s2_dict:
                s2_dict[right_char] += 1
            else:
                s2_dict[right_char] = 1
            
            # determine if a permutation exists
            # why overall O(n) even though dict evaluation is suppoed to be O(n) already?
            # in this question, there can be at most 26 keys in our dictionary
            # because there are at most 26 lowercase english alphabets
            if s1_dict == s2_dict:
                return True
            
        return False
    
s1, s2 = "ab", "eidbaooo"
s1, s2 = "ab", "eidboaoo"
s1, s2 = "a", "ab"

Solution().checkInclusion(s1, s2)