# dp - hard
class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        # solve for palindromic substring
        dp = [ [False] * n for _ in range(n) ]
        for i in range(n):
            dp[i][i] = True # single char.

        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                
                innerMatch = True
                # detect inner palindrome
                if j > i+1:
                    innerMatch = dp[i+1][j-1]

                dp[i][j] = (s[i] == s[j]) and innerMatch

        dp2 = [0] + [i for i in range(n)]
        for i in range(1, n+1):
            for j in range(1, i+1):

                if dp[j-1][i-1]:
                    if j-1 == 0:
                        dp2[i] = 0
                    else:
                        dp2[i] = min(dp2[i], dp2[j-1] + 1)

        return dp2[-1]
    
s = "a"
s = "aab"
s = "aabaa"
s = "a" * 2000 # constraint

Solution().minCut(s)