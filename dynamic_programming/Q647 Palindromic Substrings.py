# dp - medium
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # initiate a 2D dp storing whether s[i:(j+1)] is a palindrome
        # similar logic to Q5 Longest Palindromic Substring
        dp = [[False] * n for _ in range(n)]

        ans = n
        # for every single character, it's a palindrome by itself
        # and we also check for length-2 palindrome in this initialisation
        for i in range(n):

            dp[i][i] = True
            if i+1 < n and s[i] == s[i+1]:
                dp[i][i+1] = True
                ans += 1

        for l in range(2, n):
            for startIdx in range(n-l):
                if s[startIdx] == s[startIdx+l] and dp[startIdx+1][startIdx+l-1]:
                    dp[startIdx][startIdx+l] = True
                    ans += 1

        return ans
    
s = 'abc'
s = 'aaa'
s = "aabaaa"

Solution().countSubstrings(s)