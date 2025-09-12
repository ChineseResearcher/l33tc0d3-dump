# dp - medium
from typing import List
from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        wordSet = set(wordDict)

        @cache
        def recursive_build(l, r):

            ss = s[l:r+1]
            if ss in wordSet:
                return True

            curr_res = False
            # otherwise, split further
            for p in range(l+1, r+1):
                curr_res |= (recursive_build(l, p-1) and recursive_build(p, r))
                
            return curr_res

        return recursive_build(0, n-1)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Initialize DP array with False values
        dp = [False] * (len(s) + 1)
        # The empty string is always "breakable"
        dp[0] = True
        
        # Convert the wordDict to a set for faster lookup
        wordSet = set(wordDict)
        
        # Iterate over all possible substring lengths
        for i in range(1, len(s) + 1):
            # Check all possible splits of the substring s[0:i]
            for j in range(i):
                # If the substring s[j:i] is in wordSet and dp[j] is True
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # No need to check further if we've found a valid split
        
        # The result is whether the entire string can be segmented
        return dp[len(s)]
    
s, wordDict = "aaaaaaa", ["aaaa","aaa"]
s, wordDict = "leetcode", ["leet","code"]
s, wordDict = "applepenapple", ["apple","pen"]
s, wordDict = "catsandog", ["cats","dog","sand","and","cat"]

Solution().wordBreak(s, wordDict)