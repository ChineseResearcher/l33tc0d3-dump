# recursion - hard
class Solution:
    def recursiveEval(self, startIdx, s):
        currAns = 0

        i = startIdx
        while i < len(s):

            if s[i] == '(':
                bracketAns, next_i = self.recursiveEval(i+1, s)

                if i == 0 or i > 0 and s[i-1] in ['+', '(']:
                    currAns += bracketAns
                elif i > 0 and s[i-1] == '-':
                    currAns -= bracketAns

                i = next_i + 1
                continue

            if s[i] == ')':
                return currAns, i

            if s[i] not in self.operators:
                digit_stack = [s[i]]

                i_ = i
                while i_+1 < len(s) and s[i_+1] not in self.operators:
                    i_ += 1
                    digit_stack.append(s[i_])

                # add case
                if i == 0 or i > 0 and s[i-1] in ['+', '(']:
                    currAns += int(''.join(digit_stack))
                
                # subtract case
                if i > 0 and s[i-1] == '-':
                    currAns -= int(''.join(digit_stack))

                i = i_

            i += 1

        return currAns

    def calculate(self, s: str) -> int:
        # first get rid of spaces
        s = s.replace(' ', '')
        self.operators = ['+', '-', '(', ')']
        return self.recursiveEval(0, s)
    
s = "1 + 1"
s = " 2-1 + 2 "
s = "-1+2-3"
s = "(1+(4+5+2)-3)+(6+8)"
s = '-1234+(100-101)'
s = "1-(     -2)"
s = "1 + ((1 + 1) + 1)"

Solution().calculate(s)