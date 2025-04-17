# dp - hard
class Solution:
    def recursive_cnt(self, pos, tight, digitProd, digitSum):
    
        if pos == self.n:
            if digitSum > 0:
                return 1 if digitProd % digitSum == 0 else 0
            # % 0 is invalid
            else:
                return 0
        
        if (pos, tight, digitProd, digitSum) in self.dp:
            return self.dp[(pos, tight, digitProd, digitSum)]
        
        ub = self.digits[pos] if tight else 9
        
        currRes = 0
        for digit in range(0, ub + 1):
            # special attention given to case where digitProd
            # is zero as it has not decided on the starting number
            if digitSum == 0 and digit > 0:
                nextDigitProd = digit
            else:
                nextDigitProd = digitProd * digit
            
            currRes += self.recursive_cnt(pos + 1,
                                        tight and (digit == ub),
                                        nextDigitProd,
                                        digitSum + digit)
            currRes %= int(1e9 + 7)
            
        self.dp[(pos, tight, digitProd, digitSum)] = currRes
        return currRes

    def beautifulNumbers(self, l: int, r: int) -> int:
        self.n = len(str(r))
        self.digits = list(map(int, str(r)))
        self.dp = dict()
        ans_r = self.recursive_cnt(0, True, 0, 0)

        l -= 1
        self.n = len(str(l))
        self.digits = list(map(int, str(l)))
        self.dp = dict()
        ans_l = self.recursive_cnt(0, True, 0, 0)

        return (ans_r - ans_l + int(1e9 + 7)) % int(1e9 + 7)
    
l, r = 10, 20
l, r = 1, 15
l, r = 583, 623
l, r = int(1e8), int(1e9)

Solution().beautifulNumbers(l, r)