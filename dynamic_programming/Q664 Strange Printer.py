# dp - hard
class Solution:
    def recursiveForming(self, i, j):

        # it takes min. 1 print for 1 alphabet
        if i == j: return 1

        # even though we got rid of sequential duplication, it does not
        # mean we can't have repeated alphabets at some distance apart
        # i.e. soln to "abca" = soln to "abc"
        if self.s[i] == self.s[j]: return self.recursiveForming(i, j-1)

        if (i, j) in self.dp: return self.dp[(i, j)]

        # default split: split at j-1
        # add 1 because it would in the WORST case take 1 extra print to print s[j]
        # after finding out the optimal number of to print the prior s[:j]
        ans = self.recursiveForming(i, j-1) + 1

        # why only iterate to index j-2 and not j-1?
        # because after removal of sequential duplication it is impossible to
        # have repeated char at some index pair (j-1, j) anyways
        for k in range(i+1, j-1):
            
            # finding potentially better split k: i+1 <= k < j-1
            if self.s[k] == self.s[j]: 
                ans = min(ans, self.recursiveForming(i, k-1) + self.recursiveForming(k, j-1))

        # memoize
        self.dp[(i,j)] = ans

        return ans

    def strangePrinter(self, s: str) -> int:
        # it is important to observe that any sequentially duplicating alphabets
        # can be gotten rid of as the solution to "abca" & "abccca" is the same
        shortened = []
        for i in range(len(s)):

            if i > 0 and s[i] == s[i-1]: continue
            shortened.append(s[i])

        self.s = ''.join(shortened)
        self.dp = dict()

        return self.recursiveForming(0, len(self.s)-1)
    
s = "aaabbb"
s = "aba"
s = "abcabc"
s = "abcabcabc"
s = "ababc"
s = "abcdabcdabcdabcd"
s = "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa"

Solution().strangePrinter(s)