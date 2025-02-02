# dp - hard
class Solution:
    def recursiveSeq(self, sIdx, tIdx):

        # t fully matched
        if tIdx == self.n: return 1

        # exhausted all characters of s
        if sIdx == self.m: return 0

        # return memoized val.
        if (sIdx, tIdx) in self.dp: return self.dp[(sIdx, tIdx)]

        # op1: leave it
        currAns = self.recursiveSeq(sIdx+1, tIdx)

        # op2: match it
        if self.s[sIdx] == self.t[tIdx]:
            currAns += self.recursiveSeq(sIdx+1, tIdx+1)
        
        # memoize
        self.dp[(sIdx, tIdx)] = currAns

        return currAns

    def numDistinct(self, s: str, t: str) -> int:
        self.m, self.n = len(s), len(t)
        self.s, self.t = s, t

        self.dp = dict()
        return self.recursiveSeq(0, 0)

s, t = "rabbbit", "rabbit"
s, t = "babgbag", "bag"
s, t = "aabb", "ab"

Solution().numDistinct(s, t)