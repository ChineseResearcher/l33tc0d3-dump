# dp - hard
class Solution:
    def rebase(self, number, base):
        if number == 0:
            return "0"
        
        digits = []
        while number:
            digits.append(int(number % base))
            number //= base
            
        return ''.join(str(x) for x in digits[::-1])

    def recursive_cnt(self, pos, tight, lastDigit):
    
        if pos == self.n:
            return 1
        
        if (pos, tight, lastDigit) in self.dp:
            return self.dp[(pos, tight, lastDigit)]
        
        # one key observation is that k-base number representation
        # would only digits to go up to k-1
        # e.g. in base-2 representation, digits only take 0/1
        # in base-10 representation (our normal numbers), digits is in [0,9]
        ub = self.digits[pos] if tight else self.b - 1
        
        currRes = 0
        for digit in range(0, ub + 1):
            
            # we do not explore decreasing digits as per question desires
            if digit >= lastDigit:
                currRes += self.recursive_cnt(pos + 1,
                                            tight and (digit == ub),
                                            digit)
                currRes %= int(1e9 + 7)
            
        self.dp[(pos, tight, lastDigit)] = currRes
        return currRes

    def countNumbers(self, l: str, r: str, b: int) -> int:
        self.b = b
        # in order to approach this question conveniently,
        # we re-base our [l,r] bounds using the new base provided
        r_based = self.rebase(int(r), self.b)
        self.n = len(r_based)
        self.digits = list(map(int, r_based))
        self.dp = dict()
        ans_r = self.recursive_cnt(0, True, 0)

        l = str(int(l)-1)
        l_based = self.rebase(int(l), self.b)
        self.n = len(l_based)
        self.digits = list(map(int, l_based))
        self.dp = dict()
        ans_l = self.recursive_cnt(0, True, 0)

        return (ans_r - ans_l + int(1e9 + 7)) % int(1e9 + 7)
    
l, r, b = "23", "28", 8
l, r, b = "2", "7", 2
l, r, b = str(int(1e98)), str(int(1e99)), 7

Solution().countNumbers(l, r, b)