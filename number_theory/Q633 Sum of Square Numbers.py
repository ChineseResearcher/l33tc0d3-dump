# number theory - medium
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # key ideas:
        # 1) "c" <= 2^31 - 1, if there exists some "a", "b" s.t.
        # a^2 + b^2 = c, then a goes up to sqrt(c)
        # 2) as max(sqrt(c)) is roughly ~46000, a linear scan is feasible
        L = int(c ** 0.5)

        ans = False
        for a in range(L + 1):
            b_sq = c - pow(a, 2)
            if b_sq == pow(int(b_sq ** 0.5), 2):
                ans = True
                break

        return ans

c = 5
c = 9
c = 3
c = 2

Solution().judgeSquareSum(c)