# stack - medium
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        n = len(s)
        # key ideas:
        # 1) thinking greedily, as we process from left to right, the question
        # to ask is: if my curr. char. is equal or smaller than the last char. in stack,
        # can I remove that char? 
        # 2) to answer (1) we have to know the suffix frequencies of all distinct chars.

        c = Counter(s)
        ans = []         # greedy stack
        member = set()   # track added members

        for i in range(n):

            # update suffix freq.
            if i-1 >= 0:
                c[s[i-1]] -= 1

            x = s[i]
            if x in member:
                continue

            while ans and ord(x) < ord(ans[-1]) and c[ans[-1]] > 0:
                member.discard(ans.pop())
            ans.append(x)
            member.add(x) 

        return ''.join(ans)
    
s = "abacb"
s = "bcabc"
s = "bbcaac"
s = "cbacdcbc"
s = "cdadabcc"
s = "leetcode"

Solution().removeDuplicateLetters(s)