# backtracking - medium
from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        # n is max. 1e6, which means there are at most 8 digits needed
        # for small input like this, we can use backtrack to brute-force
        s = str(n)
        m = len(s)

        # one challenge is to realise that for a number n, w/ str length m
        # if n > 'm' * m, e.g 4455 > '4' * 4 = 4444, then it would not be able
        # to have the next numerically balanced number w/ only length 4
        if n >= int(str(m) * m):
            L = m + 1
        else:
            L = m

        self.ans = None
        def backtrack(numStr, tight):

            global ans
            if len(numStr) == L:

                valid = True
                # validate if it's balanced
                for k, v in Counter(numStr).items():
                    if int(k) != v:
                        valid = False
                        break

                if int(''.join(numStr)) <= n:
                    valid = False

                if valid:
                    self.ans = numStr[:]
                return

            # '0' is naturally not an option as choosing '0' already exceeds 0 times
            # determine our position using length of the stack
            pos = len(numStr)

            # if we are 'bounded', i.e. L = m
            if tight:
                lb = int(s[pos])
            else:
                lb = 1

            for digit in range(max(lb, 1), 10):

                numStr.append(str(digit))
                if L == m:
                    backtrack(numStr, tight and (int(s[pos]) == digit))
                else:
                    backtrack(numStr, tight)

                numStr.pop()

                # early stop
                if self.ans:
                    break

        _ = backtrack([], True if L == m else False)
        return int(''.join(self.ans))
    
n = 1
n = 188
n = 212
n = 238
n = 1000
n = 3000
n = 4444
n = 999999
n = int(1e6)

Solution().nextBeautifulNumber(n)