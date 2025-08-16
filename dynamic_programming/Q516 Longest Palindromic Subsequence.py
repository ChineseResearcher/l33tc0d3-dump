# dp - medium

# bottom-up
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # 2-D dp to store the length of longest palindrome subsequence for s[i:j+1] 
        # e.g. if s = 'bbbab', dp[0][3] = 3 as the longest palindrome subsequence
        # for "bbba" is "bbb"
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            # all single char are palindromes
            dp[i][i] = 1

        for length in range(2,n+1):
            for j in range(n-length+1):
                
                start = j
                end = start + length - 1

                # inner match + outer match
                op1 = 2 * int(s[start] == s[end]) + dp[start+1][end-1]

                # left bound match
                op2 = dp[start][end-1]

                # right bound match
                op3 = dp[start+1][end]

                dp[start][end] = max(op1, max(op2, op3))

        return dp[0][n-1]
    
# top-down
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        dp = [ [None] * n for _ in range(n) ]

        def recursive_form(l, r):

            if l == r:
                return 1
            
            if l > r:
                return 0

            if dp[l][r] != None:
                return dp[l][r]

            curr_res = 0
            op1 = 0
            if int(s[l] == s[r]):
                op1 = 2 + recursive_form(l+1, r-1)

            op2 = recursive_form(l+1, r) # skip s[l]
            op3 = recursive_form(l, r-1) # skip s[r]

            curr_res = max(op1, max(op2, op3))
            dp[l][r] = curr_res
            
            return curr_res

        return recursive_form(0, n-1)
    
s = "bbbab"
s = "cbbd"
s = "abcabcabcabc"
s = "a" * 1000 # constraint

Solution().longestPalindromeSubseq(s)