# dp - hard
class Solution:
    def recursive_del_op(self, startIdx):

        if startIdx == self.n:
            return 0

        if startIdx in self.dp: return self.dp[startIdx]
        
        # op1: just delete entire string
        currAns = 1

        # op2: explore possible repeated prefix
        for i in range(startIdx, startIdx + (self.n-startIdx) // 2):

            # there's is need to optimise with KMP here, but lazy to do it
            # since the curr. form also passes with O(2^N) complexity
            if self.s[startIdx : (i+1)] == self.s[(i+1) : startIdx + 2*(i+1-startIdx)]:
                currAns = max(currAns, 1 + self.recursive_del_op(i+1))

        self.dp[startIdx] = currAns

        return currAns

    def deleteString(self, s: str) -> int:
        self.n = len(s)
        self.s = s

        self.dp = dict()
        return self.recursive_del_op(0)
    
s = "abcabcdabc"
s = "aaabaab"
s = "aaaaa"

Solution().deleteString(s)