# stack - easy
class Solution:
    def clearDigits(self, s: str) -> str:
        digits = set(['0','1','2','3','4','5','6','7','8','9'])

        stack = []
        for char in s:

            if char in digits:
                if stack: stack.pop()
            
            else:
                stack.append(char)

        return ''.join(stack)
    
s = "cb34"
Solution().clearDigits(s)