# backtracking - medium
class Solution:
    def backtrack(self, currIP, startIdx):
    
        if startIdx == self.n:
            # only valid if we have four integer strings
            if len(currIP) == 4:
                self.ans.append('.'.join(currIP[:]))
            return
        
        # prune the case where the remaining length is definitely
        # not possible to be distributed correctly
        if self.n - startIdx > (4 - len(currIP)) * 3:
            return
        
        # if startIdx falls on "0", it must be the current integer
        if self.s[startIdx] == '0':
            currIP.append('0')
            self.backtrack(currIP, startIdx+1)
            currIP.pop()
        
        else:
            for i in range(startIdx, self.n):
                if 0 < int(self.s[startIdx:i+1]) <= 255:
                    currIP.append(self.s[startIdx:i+1])
                    self.backtrack(currIP, i+1)
                    currIP.pop()

    def restoreIpAddresses(self, s):
        self.s, self.n = s, len(s)
        self.ans = []

        self.backtrack([], 0)
        return self.ans
    
s = "25525511135"
s = "0000"
s = "101023"

Solution().restoreIpAddresses(s)