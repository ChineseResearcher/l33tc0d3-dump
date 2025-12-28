# dp - hard
from functools import cache
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        n = len(words)
        words.sort(key=lambda x:len(x))

        built = set()
        # find shortest length of words and first add them to built
        sl = len(words[0])
        idx = 0
        while idx < n and len(words[idx]) == sl:
            built.add(words[idx])
            idx += 1

        @cache
        def f(w: str) -> bool:

            if w in built:
                return True
            
            res = False
            # partition DP
            for p in range(1,len(w)):
                res |= (f(w[:p]) and f(w[p:]))
                if res:
                    break
            
            return res

        ans = []
        for i in range(idx, n):
            if f(words[i]):
                ans.append(words[i])

            f.cache_clear()
            # add to built
            built.add(words[i])

        return ans
    
words = ["cat","dog","catdog"]
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Solution().findAllConcatenatedWordsInADict(words)