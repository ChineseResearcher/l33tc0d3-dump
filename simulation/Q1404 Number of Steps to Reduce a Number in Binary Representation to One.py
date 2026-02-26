# simulation - medium
class Solution:
    def numSteps(self, s: str) -> int:

        # key ideas:
        # 1) s is too big (up to 500 in length) to directly store as an integer
        # 2) use right shift and carry-addition of 1 bit from right-end to 
        # simulate the division by 2 and addition of 1
        # 3) curr. number is even if s[-1] = '0' else odd

        ans = 0
        while s != '1':

            # even: division by 2
            if s[-1] == '0':
                s = s[:-1]

            # odd: add 1 from right-end
            else:
                idx = len(s)-1
                while idx >= 0 and s[idx] != '0':
                    idx -= 1

                # case of all '1's e.g. 0b1111
                if idx == -1:
                    s = '1' + '0' * len(s)
                else:
                    s = s[:idx] + '1' + '0' * (len(s) - idx - 1)

            # increment ops
            ans += 1

        return ans

s = "1"
s = "10"
s = "1101"

Solution().numSteps(s)