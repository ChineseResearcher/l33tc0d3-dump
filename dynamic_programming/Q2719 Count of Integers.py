# dp - hard
class Solution:
    def recursive_count(self, pos, tight, digitSum):
    
        if pos == self.n:
            # breached indicate whether the formed number
            # still within the range [min_sum, max_sum]
            return 1 if self.min_sum <= digitSum <= self.max_sum else 0
        
        if (pos, tight, digitSum) in self.dp: return self.dp[(pos, tight, digitSum)]
        
        # we only  explore up to digit at num2[pos] if we are currently "tight"
        high = self.digit_ceil[pos] if tight else 9
        
        curr_res = 0
        for digit in range(0, high + 1):
            curr_res += self.recursive_count(pos + 1, 
                                            tight and (digit == high),
                                            digitSum + digit)
            # curr_res %= int(1e9 + 7)
        
        self.dp[(pos, tight, digitSum)] = curr_res
        return curr_res

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:

        self.min_sum, self.max_sum = min_sum, max_sum

        # subproblem 1: up to num2
        self.n = len(num2)
        self.digit_ceil = list(map(int, num2))
        self.dp = dict()
        ans_max = self.recursive_count(0, True, 0)

        # subproblem 2: up to num1 - 1
        num1 = str(int(num1) - 1)
        self.n = len(num1)
        self.digit_ceil = list(map(int, num1))
        self.dp = dict()
        ans_min = self.recursive_count(0, True, 0)

        return (ans_max - ans_min) % int(1e9 + 7)
    
num1, num2, min_sum, max_sum = "1", "12", 1, 8
num1, num2, min_sum, max_sum = "1", "5", 1, 5
num1, num2, min_sum, max_sum = "4179205230", "7748704426", 8, 46

Solution().count(num1, num2, min_sum, max_sum)