# string - medium
from typing import List
import re 
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        exact_match = set(wordlist)
        cap_match = dict()
        # we could encode vowels as wildcard "*"
        # e.g. "frank" becomes "fr*nk"
        vowel_match = dict()

        for w in wordlist:

            w_l = w.lower()
            if w_l not in cap_match:
                cap_match[w_l] = []
            cap_match[w_l].append(w)

            # lowercased + replace vowels w/ wildcard
            w_l_v = re.sub(r'[aeiou]', '*', w_l)
            if w_l_v not in vowel_match:
                vowel_match[w_l_v] = []
            vowel_match[w_l_v].append(w)

        ans = []
        for q in queries:

            if q in exact_match:
                ans.append(q)
                continue
            
            # if case-insensitive version of queried word
            # gets matched as a lowercase, get the first-in-order original word
            q_l = q.lower()
            if q_l in cap_match:
                ans.append(cap_match[q_l][0])
                continue
            
            # in addition, replace vowels w/ wildcard to see if matched
            q_l_v = re.sub(r'[aeiou]', '*', q_l)
            if q_l_v in vowel_match:
                ans.append(vowel_match[q_l_v][0])
                continue
            
            # otherwise, no answer
            ans.append('')
                
        return ans
    
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

wordlist = ["ae", "aa"]
queries = ["UU"]

Solution().spellchecker(wordlist, queries)