# stack - hard
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # there can be multiple regions of valid parantheses of diff. lengths
        # here we could use a stack of record such diff. lengths
        bracket_st, length_st = [], []

        ans = 0
        for char in s:

            # if curr. bracket stack is empty OR no valid close bracket formed
            if not bracket_st or (bracket_st and (bracket_st[-1] != '(' or char != ')')):
                bracket_st.append(char)
                length_st.append(-1)
                continue

            # otherwise, we must have a valid close bracket
            bracket_st.pop()

            joined_length = 0
            # there must be a unclosed state denoted by -1 in length_stack
            while length_st[-1] != -1:
                joined_length += length_st.pop()

            # acknowledge the curr. bracket
            length_st[-1] = 2

            while length_st and length_st[-1] != -1:
                joined_length += length_st.pop()

            # append the final joined length
            length_st.append(joined_length)

            ans = max(ans, length_st[-1])

        return ans
    
s = "(()((())"
s = "(()"
s = ")()())"
s = ""

Solution().longestValidParentheses(s)