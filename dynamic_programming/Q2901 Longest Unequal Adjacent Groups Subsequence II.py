# dp - medium
from typing import List
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        # initiate dp arr of length n, where dp[i] stores 
        # the best subseq. if we consider up to words[:i]
        dp = [ [words[i]] for i in range(n) ]

        def hd(str1, str2):
            # return hamming distance of two equal-length strings
            d = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    d += 1
            return d

        best_len, ans = 1, dp[0] 
        for i in range(1, n):
            
            curr_best_len, curr_best = 0, None
            for j in range(i):
                
                # three conditions to check
                # 1) must be in diff. groups
                # 2) must be of same word length
                # 3) hamming distance = 1
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and \
                hd(words[i], words[j]) == 1:
                    
                    if len(dp[j]) > curr_best_len:
                        curr_best = j
                        curr_best_len = len(dp[j])
                        
            if curr_best is not None:
                new = dp[curr_best][:]
                new.append(words[i])
                
                dp[i] = new
                
            if len(dp[i]) > best_len:
                ans = dp[i]
                best_len = len(dp[i])
                
        return ans
    
words, groups = ["bab","dab","cab"], [1,2,2]
words, groups = ["a","b","c","d"], [1,2,3,4]

Solution().getWordsInLongestSubsequence(words, groups)