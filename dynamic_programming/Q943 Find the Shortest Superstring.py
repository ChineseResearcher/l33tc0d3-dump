# dp - hard
from typing import List
from functools import cache
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        
        n = len(words)
        # core ideas:
        # 1) use a bitmask to represent the words that have yet to be included
        # e.g. if there 5 words, bitmask 0b11110 would indicate the first word have yet to be included
        # 2) prefix overlap if possible to obtain the shortest string possible
        # e.g. if previous word was 'abc', and next candidate is 'bca', we could re-use the 'bc'"4. Internal Control Report.pdf"

        # helper for (2)
        def trim_overlap_prefix(prevWord, currWord):

            m = len(currWord)
            for i in range(m+1, 0, -1):
                if currWord[:i] == prevWord[-i:]:
                    return currWord[i:]
                
            return currWord

        @cache
        def recursive_build(mask, prev):

            if mask == (1 << n) - 1:
                return ''
            
            curr_res, best_len = '', float('inf')
            for i in range(n):
                # get missing word
                if mask & (1 << i) == 0:
                    
                    # update mask
                    mask |= (1 << i)

                    substr1 = trim_overlap_prefix(words[prev], words[i]) if prev != -1 else words[i]
                    substr2 = recursive_build(mask, i)
                    curr_str = substr1 + substr2
                            
                    if len(curr_str) < best_len:
                        curr_res = curr_str
                        best_len = len(curr_str)

                    # roll-back mask update
                    mask &= ~(1 << i)

            return curr_res

        return recursive_build(0, -1)
    
words = ["alex","loves","leetcode"]
words = ["catg","ctaagt","gcta","ttca","atgcatc"]

Solution().shortestSuperstring(words)