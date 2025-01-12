# stack - medium
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # initiate a stack to handle bracket parsing
        stack = []
        # intiate a set storing the indices of brackets that are valid
        valid_brackets = set()

        for idx, char in enumerate(s):

            if char not in ['(', ')']:
                continue

            # invalid right bracket
            if not stack and char == ')':
                continue

            if char == '(': stack.append([char, idx])
            # any left bracket would be consumed
            if char == ')':
                # a pair of '(' and ')' has been encountered
                # and they would be added to valid
                valid_brackets.add(stack[-1][1])
                valid_brackets.add(idx)

                stack.pop()

        ans = []
        for idx, char in enumerate(s):

            if char not in ['(', ')']: 
                ans.append(char)
                continue

            if idx in valid_brackets:
                ans.append(char)

        return ''.join(ans)

s = "lee(t(c)o)de)"
s = "a)b(c)d"
s = "))(("

Solution().minRemoveToMakeValid(s)