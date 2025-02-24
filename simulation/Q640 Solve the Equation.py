# simulation - medium
class Solution:
    def processing(self, expr):
        # given a string expression of either lhs or rhs or an equation
        # return the sum of constants and coeffs
        coeff, constant = 0, 0
        
        if expr[0] != '-':
            expr = '+' + expr
        
        expr += '+'
        
        window, last_op = [], expr[0]
        for char in expr[1:]:
            if char in ['+','-']:
                
                if last_op == '+':
                    if window[-1] != 'x':
                        constant += int(''.join(window))
                    else:
                        coeff += int(''.join(window[:-1])) if len(window) > 1 else 1
        
                else:
                    if window[-1] != 'x':
                        constant -= int(''.join(window))
                    else:
                        coeff -= int(''.join(window[:-1])) if len(window) > 1 else 1
        
                window = []
                last_op = char
        
            elif char not in ['+','-']:
                window.append(char)
                        
        return constant, coeff

    def solveEquation(self, equation: str) -> str:
        
        lhs, rhs = equation.split('=')[0], equation.split('=')[1]

        lhs_const, lhs_coeff = self.processing(lhs)
        rhs_const, rhs_coeff = self.processing(rhs)

        const_sum = lhs_const - rhs_const
        coeff_sum = rhs_coeff - lhs_coeff

        if coeff_sum == 0 and const_sum == coeff_sum:
            return 'Infinite solutions'
        if coeff_sum == 0 and const_sum != coeff_sum:
            return 'No solution'

        return "x=" + str(int(const_sum/coeff_sum))
    
equation = "x+5-3+x=6+x-2"
equation = "x=x"
equation = "2x=x"

Solution().solveEquation(equation)