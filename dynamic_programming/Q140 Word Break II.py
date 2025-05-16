# dp - hard
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # set the wordDict for efficient lookup
        wordSet = set(wordDict)

        def recursive_form(startIdx, breaks):
            
            if startIdx == n:
                return ['']
            
            if (startIdx, breaks) in dp:
                return dp[(startIdx, breaks)]
            
            curr_ans = []
            for i in range(startIdx, n):
                
                if s[startIdx: i+1] in wordSet:
                    curr = [s[startIdx: i+1]]
                    
                    next_ans = recursive_form(i+1, breaks+1)
                    if next_ans:
                        for comb in next_ans:
                            
                            next_pattern = ' '.join(comb).rstrip(' ')
                            if next_pattern:
                                curr.append(next_pattern)

                            curr_ans.append(curr[:])

                            # backtracking
                            if next_pattern:
                                curr.pop()
                        
            dp[(startIdx, breaks)] = curr_ans
            return curr_ans

        n = len(s)

        dp = dict()
        res = recursive_form(0, 0)
 
        ans = []
        # because the first word has not yet properly joined w/ the rest
        for comb in res:
            ans.append(' '.join(comb))
            
        return ans
    
s, wordDict = "catsanddog", ["cat","cats","and","sand","dog"]
s, wordDict = "pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]
s, wordDict = "catsandog", ["cats","dog","sand","and","cat"]
# solution should be efficient for n = 100
s, wordDict = "catog" * 20, ["cat","og"]

Solution().wordBreak(s, wordDict)