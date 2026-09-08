# number theory - medium
class Solution:
    def countCommas(self, n: int) -> int:

        # key ideas:
        # 1) observe that (999, 999999] uses 1 comma, (999999, 999999999] uses 2 commas
        # 2) since n max out at 1e15, we only need to perform comma accounting
        # for discrete ranges available up to n

        mul = 2
        curr, prev = pow(10, 3 * mul) - 1, pow(10, 3 * (mul - 1)) - 1

        ans = 0
        while n >= curr:

            ans += (curr - prev) * (mul - 1)
            prev = curr
            mul += 1
            curr = pow(10, 3 * mul) - 1

        ans += max((n - prev), 0) * (mul - 1)
        return ans

n = 998
n = 1002
n = int(1e15)

Solution().countCommas(n)