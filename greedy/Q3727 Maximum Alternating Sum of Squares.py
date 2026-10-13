# greedy - medium
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:

        n = len(nums)
        m = n // 2
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) counting sort for range [0, 4 * 1e4]
        # 2) assign n // 2 elements to be carrying minus sign, the rest is added to the sum
        hi = 0
        for x in nums:
            hi = fmax(hi, abs(x))

        F, S = [0] * (hi + 1), set()
        for x in nums:
            ax = abs(x)
            F[ax] += 1
            S.add(ax)

        pfCnt, ans = 0, 0
        for x in sorted(S):
            if pfCnt < m:
                if pfCnt + F[x] > m:
                    ans -= (m - pfCnt) * pow(x, 2)
                    ans += (pfCnt + F[x] - m) * pow(x, 2)
                else:
                    ans -= F[x] * pow(x, 2)
            else:
                ans += F[x] * pow(x, 2)

            pfCnt += F[x]

        return ans

nums = [7,19]
nums = [1,2,3]
nums = [1,-1,2,-2,3,-3]

Solution().maxAlternatingSum(nums)