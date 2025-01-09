# backtracking - medium
class Solution:
    def valid_bracket(self, bracket_string):

        # this helper function checks for the validity of partial brackets as well
        # initiate two vars to keep track of the current left bracket & right bracket counts
        l_b_cnt, r_b_cnt = 0, 0
        for char in bracket_string:
            l_b_cnt += 1 if char == '(' else 0
            r_b_cnt += 1 if char == ')' else 0
            if r_b_cnt > l_b_cnt:
                return False
        return True

    def form_brackets(self, bracket_string):

        n = self.n
        # terminating bad case: too many brackets OR invalid brackets
        l_b_cnt, r_b_cnt = bracket_string.count('('), bracket_string.count(')')
        if l_b_cnt > n or r_b_cnt > n or not self.valid_bracket(bracket_string):
            return
        # terminating good case: we've found a valid form of n brackets   
        if l_b_cnt == r_b_cnt == n and self.valid_bracket(bracket_string):
            self.solutions.append(bracket_string)
            return

        for b in ['(',')']:
            self.decisions.append(b)
            self.form_brackets(bracket_string + b)
            self.decisions.pop()

    def generateParenthesis(self, n):

        self.n = n
        self.solutions, self.decisions = [], []
        self.form_brackets('')
        return self.solutions

n = 3
Solution().generateParenthesis(n)