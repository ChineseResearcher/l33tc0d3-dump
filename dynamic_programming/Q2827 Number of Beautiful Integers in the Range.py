# dp - hard
class Solution:
    def recursive_int(self, pos, tight, startPos, oddCnt, remainder):

        # a beautiful integer has to have:
        # 1) same number of odd & even digits
        # 2) divisible by k
        # note: the integer has no leading 0s
        if pos == self.n:
            if startPos > -1:
                return 1 if remainder == 0 and oddCnt == (self.n-startPos) // 2 else 0
            else:
                return 0
        
        if (pos, tight, startPos, oddCnt, remainder) in self.dp:
            return self.dp[(pos, tight, startPos, oddCnt, remainder)]
        
        upper_bound = self.digits[pos] if tight else 9
        
        curr_res = 0
        for digit in range(0, upper_bound + 1):
            # there's no point to explore odd-length numStr
            if startPos == -1 and digit > 0 and (self.n-pos) % 2 != 0:
                continue
            
            next_remainder = (remainder + digit * pow(10, self.n-pos-1)) % self.k
            curr_res += self.recursive_int(pos + 1,
                                        tight and (digit == upper_bound),
                                        pos if startPos == -1 and digit > 0 else startPos,
                                        oddCnt + 1 if digit % 2 != 0 else oddCnt,
                                        next_remainder)
            curr_res %= int(1e9 + 7)
            
        self.dp[(pos, tight, startPos, oddCnt, remainder)] = curr_res
        return curr_res

    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        self.k = k

        high = str(high)
        self.n = len(high)
        self.digits = list(map(int, high))
        self.dp = dict()

        ans_high = self.recursive_int(0, True, -1, 0, 0)

        low = str(low - 1)
        self.n = len(low)
        self.digits = list(map(int, low))
        self.dp = dict()

        ans_low = self.recursive_int(0, True, -1, 0, 0)

        return (ans_high - ans_low + int(1e9 + 7)) % int(1e9 + 7)
    
low, high, k = 10, 20, 3
low, high, k = 1, 10, 1
low, high, k = 5, 5, 2
low, high, k = int(1e7), int(1e9), 13

Solution().numberOfBeautifulIntegers(low, high, k)