# stack - medium
from string import ascii_lowercase as lwc
from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:

        # maintain a frequency count of active section of s as we are "removing" head of s 
        c_freq = Counter(s)

        # maintain a stack that simulates t_string
        t = []

        def canPop(char, freq):

            # test if there's still a smaller element 
            # in the active section w/ cnt > 0
            for i in range(ord(char) - ord('a') - 1, -1, -1):
                if freq[lwc[i]] > 0:
                    return False
                
            return True
        
        ans = []
        for c in s:

            # discard curr. char
            c_freq[c] -= 1

            if not t:
                t.append(c)
                continue

            # apply greedy thinking:
            # how to determine if the top of t needs to be popped now instead of later?
            # check if there are still elements smaller than it w/ cnt > 0 in the unprocessed section
            used = False
            while t and canPop(t[-1], c_freq):

                # we could possibly insert curr. character c as well
                if not used and (ord(ans[-1]) if ans else ord("a")) <= ord(c) <= (ord(t[-1]) if t else ord("z")):
                    ans.append(c)
                    used = True

                ans.append(t.pop())
            
            if not used:
                t.append(c)

        # write remaining in stack t
        ans.extend(t[::-1])

        return ''.join(ans)
    
s = "bdda"
s = "bac"
s = "zza"
s = "vzhofnpo"
s = "mmuqezwmomeplrtskz"
s = "evokzbuginbpptrfaamp"

Solution().robotWithString(s)