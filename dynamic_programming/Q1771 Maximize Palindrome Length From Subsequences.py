# dp - hard
from functools import cache
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        # if we join word1 and word2 together, it's like solving 
        # longest palindromic subsequence (LPS) w/ an additional constraint
        # s.t. both word1 and word2 have to contribute at least one char to the palindrome
        joinStr = word1 + word2

        # modified LPS:
        # the core idea is to maintain an additional boolean variable
        # to indicate if we have already included at least one char from each word
        # when it is the case, non_empty is set to True
        @cache
        def recursive_form(l, r, non_empty):

            if l == r:
                return int(non_empty) 
            
            if l > r:
                return 0

            # there's no need to address the subproblem (l, r)
            # where we had not yet picked at least one char from each word
            # and (l, r) is already constrained to [0...m-1] or [m...m+n-1] 
            if not non_empty and (l >= m or r < m):
                return 0
            
            # case where we match at least one char from each word
            if joinStr[l] == joinStr[r] and (non_empty or l < m <= r):
                return 2 + recursive_form(l+1, r-1, True)

            skip_l = recursive_form(l+1, r, non_empty) # skip joinStr[l]
            skip_r = recursive_form(l, r-1, non_empty) # skip joinStr[r]

            return max(skip_l, skip_r)

        return recursive_form(0, m+n-1, False)
    
word1, word2 = "cacb", "cbba"
word1, word2 = "ab", "ab"
word1, word2 = "aa", "bb"
word1, word2 = "a" * 500, "a" * 500 # constraint

Solution().longestPalindrome(word1, word2)