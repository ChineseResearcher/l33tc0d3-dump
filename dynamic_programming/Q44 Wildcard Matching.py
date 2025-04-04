# dp - hard
class Solution:
    def recursiveMatch(self, s_idx, p_idx):

        if s_idx == self.m and (p_idx == self.n or (p_idx == self.n-1 and self.p[p_idx] == '*')):
            return True
        
        # false cases:
        # 1) s exhausted before p: s = 'acdcb', p = 'a*c?b', with 
        # the exception that we are at the last char of p and it is '*'
        # 2) p exhausted before s: s = 'aa', p = 'a'
        if (s_idx < self.m and p_idx == self.n) or \
            (s_idx == self.m and p_idx < self.n):
            return False
    
        if (s_idx, p_idx) in self.dp: return self.dp[(s_idx, p_idx)]
        
        currAns = False
        # depending on the curr. p char, we explore recursive cases
        # 1) op1: match the curr. s char
        if self.p[p_idx] == self.s[s_idx] or self.p[p_idx] == '?':
            currAns = (currAns or self.recursiveMatch(s_idx+1, p_idx+1))

        # 2) op2: with '*' operator, we could match 0 to inf. characters in s
        elif self.p[p_idx] == '*':
            for matchIdx in range(s_idx, self.m+1):
                currAns = (currAns or self.recursiveMatch(matchIdx, p_idx+1))
                # early stop
                if currAns:
                    break

        # memoize
        self.dp[(s_idx, p_idx)] = currAns
        return currAns

    def isMatch(self, s: str, p: str) -> bool:
        # '*' can appear multiple times in a row
        # multiple '*' is equivalent to one single '*'

        processed_p = []
        for idx, char in enumerate(p):
            # compress multiple '*' into one
            if idx > 0 and p[idx] == '*' and p[idx-1] == '*':
                continue

            processed_p.append(char)

        p = ''.join(processed_p)
        # edge case: s is empty
        if not s:
            return True if (not p or (len(p) == 1 and p[0] == '*')) else False

        self.m, self.n = len(s), len(p)
        self.s, self.p = s, p

        self.dp = dict()
        return self.recursiveMatch(0, 0)
    
s, p = "aa", "a"
s, p = "aa", "*"
s, p = "cb", "?a"
s, p = 'acdcb', 'a*c?b'
s, p = "adceb", "*a*b"
s, p = "adceb", "*a?b"
s, p = "adceb", "?a*b"
s, p = "adceb", "a?c??"
s, p = "", "***"
s, p = "", ""
s, p = "aa", "*aaa*"
s, p = "abcabczzzde", "*abc???de*"

Solution().isMatch(s, p)