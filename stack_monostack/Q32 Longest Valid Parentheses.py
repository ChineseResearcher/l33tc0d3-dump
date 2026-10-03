# stack - hard
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) 2 stacks: 1st tracks unmatched brackets, 2nd tracks lengths of valid parentheses
        # 2) set every () pair's length to 2, and merge it w/ adjacenet
        bracket_st, length_st = [], []

        ans = 0
        for c in s:
            
            x, y = bracket_st[-1] if bracket_st else '', c
            # if curr. bracket stack is empty OR no valid close bracket formed
            if (x, y) != ('(', ')'):
                bracket_st.append(c)
                length_st.append(-1)
                continue

            # otherwise, we must have a valid close bracket
            bracket_st.pop()

            l = 0
            # there must be a unclosed state denoted by -1 in length_stack
            while length_st[-1] != -1:
                l += length_st.pop()

            # acknowledge the curr. bracket
            length_st[-1] = 2
            while length_st and length_st[-1] != -1:
                l += length_st.pop()

            # append the final joined length
            length_st.append(l)
            ans = fmax(ans, length_st[-1])

        return ans
    
s = ""
s = "(()"
s = ")()())"
s = "(()((())"

Solution().longestValidParentheses(s)