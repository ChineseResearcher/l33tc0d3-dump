# dp - hard
class Solution:
    def recursive_form(self, pos, tight, lastDigit):

        if pos == self.n:
            return 1

        if (pos, tight, lastDigit) in self.dp: return self.dp[(pos, tight, lastDigit)]
        upper_bound = self.digits[pos] if tight else 9

        curr_cnt = 0
        for digit in range(0, upper_bound+1):
            if not lastDigit or abs(digit - int(lastDigit)) == 1:
                if not lastDigit and digit == 0:
                    nextDigit = ''
                else:
                    nextDigit = str(digit)

                curr_cnt += self.recursive_form(pos + 1, 
                                            tight and (digit == upper_bound), 
                                            nextDigit)
                curr_cnt %= int(1e9 + 7)

        self.dp[(pos, tight, lastDigit)] = curr_cnt
        return curr_cnt

    def countSteppingNumbers(self, low: str, high: str) -> int:
        # get ans for subproblem up to high
        self.n = len(high)
        self.dp = dict()
        self.digits = list(map(int, high))

        ans_high = self.recursive_form(0, True, '')

        # get ans for subproblem up to low-1
        low = str(int(low) - 1)
        self.n = len(low)
        self.dp = dict()
        self.digits = list(map(int, low))

        ans_low = self.recursive_form(0, True, '')

        return (ans_high - ans_low + int(1e9 + 7)) % int(1e9 + 7)
    
low, high = "1", "11"
low, high = "90", "101"
low, high = "43493", "280549"
low, high = "125319", "196678"
low, high = "74516181", "7925704418"
low, high = "1603909526", "6292084825"
low, high = "9" * 90, "9" * 91

Solution().countSteppingNumbers(low, high)