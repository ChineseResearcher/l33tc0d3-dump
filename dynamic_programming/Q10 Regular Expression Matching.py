# dp - hard
class Solution:
    def recursiveMatch(self, s_idx, p_idx):
        
        if s_idx == self.m and p_idx == self.n:
            return True
        
        # false case:
        # 1) pattern length exhausted but s length hasn't
        # 2) s length exhausted but pattern length has not, with the exception that
        # we are at the second last char. of pattern and the last pattern char is '*'
        if (s_idx == self.m and p_idx+1 < self.n and self.p[p_idx+1] != '*') or \
           (s_idx < self.m and p_idx == self.n):
            return False

        if (s_idx, p_idx) in self.dp: return self.dp[(s_idx, p_idx)]
        
        currRes = False
        # check if curr s char matches curr p char exactly OR curr p char is a wildcard
        if s_idx < self.m and (self.s[s_idx] == self.p[p_idx] or self.p[p_idx] == '.'):
            
            # a new pointer to be incremeted for s index
            s_idx_n = s_idx
            # detect if next p char is a '*'
            if p_idx + 1 < self.n and self.p[p_idx + 1] == '*':
                while True:

                    if s_idx_n < self.m and (self.s[s_idx_n] == self.p[p_idx] or self.p[p_idx] == '.'):
                        s_idx_n += 1
                    else:
                        break
                
                    currRes = (currRes or self.recursiveMatch(s_idx_n, p_idx+2))
        
            else:
                currRes = (currRes or self.recursiveMatch(s_idx+1, p_idx+1))

        # if next p char is '*', we always have the freedom to skip curr p char
        if p_idx + 1 < self.n and self.p[p_idx + 1] == '*':
            # skip curr. p char
            currRes = (currRes or self.recursiveMatch(s_idx, p_idx+2))

        # memoize
        self.dp[(s_idx, p_idx)] = currRes

        return currRes
        
    def isMatch(self, s: str, p: str) -> bool:
        # notice from one TC that '*' can appear multiple times in a row
        # multiple '*' is equivalent to one single '*'
        # leading '*' are also not useful

        processed_p = []
        for idx, char in enumerate(p):
            # compress multiple '*' into one
            if idx > 0 and p[idx] == '*' and p[idx-1] == '*':
                continue

            processed_p.append(char)
            # remove leading '*'
            if len(processed_p) == 1 and processed_p[-1] == '*':
                processed_p.pop()

        p = ''.join(processed_p)

        self.m, self.n = len(s), len(p)
        self.s, self.p = s, p

        self.dp = dict()
        return self.recursiveMatch(0, 0)

s, p = "abc", "a***abc" # '***' matches 'a', with the later two '*' matching '' empty strings
s, p = "aab", "c*a*b"
s, p = "ab", ".*"
s, p = "aaa", "ab*ac*a"
s, p = "mississippi", "mis*is*p*."
s, p = "aaa", "a*a"
s, p = "a", "ab*"
s, p = "a", "a." # '.' only matches a valid char, cannot match empty string

Solution().isMatch(s, p)