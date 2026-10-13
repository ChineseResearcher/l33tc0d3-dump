# counting - medium
class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:

        m = len(rolls)
        # key ideas:
        # 1) goal is to build an array with 1 <= arr[i] <= 6, arr.length = n, sum(arr) = T
        # 2) T is backed out from mean, n, m, and sum of m rolls

        T = mean * (n + m) - sum(rolls)

        a, b = T // n, T % n
        ans = [a] * n
        # distribute the modulo
        if b > 0:
            for i in range(b):
                ans[i] += 1

        # sanity check on the range bounds of each value
        for x in ans:
            if 1 <= x <= 6:
                continue
            return []

        return ans

rolls, mean, n = [1,5,6], 3, 4
rolls, mean, n = [3,2,4,3], 4, 2
rolls, mean, n = [1,2,3,4], 6, 4

Solution().missingRolls(rolls, mean, n)