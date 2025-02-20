# monotonic stack - medium
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Initialize the stack and other necessary data structures
        stack = []
        in_stack = set()  # To check if a character is already in the stack
        char_count = {}  # To store the frequency of each character in the string

        # Count the frequency of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Iterate over each character in the string
        for char in s:
            # Decrease the count of the current character
            char_count[char] -= 1

            # If the character is already in the stack, skip it
            if char in in_stack:
                continue

            # While the stack is not empty and the top character of the stack is
            # greater than the current character and the top character of the stack
            # will appear later in the string, pop the stack
            while stack and stack[-1] > char and char_count[stack[-1]] > 0:
                in_stack.remove(stack.pop())

            # Add the current character to the stack and mark it as added by adding to set
            stack.append(char)
            in_stack.add(char)

        # Join the characters in the stack to form the result string
        return ''.join(stack)
    
s = "bcabc"
s = "cbacdcbc"

Solution().removeDuplicateLetters(s)