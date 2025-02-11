# stack - medium
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m, n = len(s), len(part)
        # initiate a stack to store characters of s from left to right
        stack = []

        for i in range(m):

            stack.append(s[i])
            if len(stack) >= n and ''.join(stack[-n:]) == part:
                j = 0
                while j < n:
                    stack.pop()
                    j += 1

        return ''.join(stack)
    
s, part = "missisipipii", "sipi"
s, part = "daabcbaabcbc", "abc"
s, part = "cabababa", "abcc"

Solution().removeOccurrences(s, part)