# dp - hard
from functools import cache
from collections import defaultdict
divisor = defaultdict(list)
# pre-compute the divisors for length in range [1, 200]
for ll in range(1, 201):
    if ll > 1:
        divisor[ll].append(1)
    for d in range(2, ll):
        if ll % d: continue
        inv_d = ll // d
        if d > inv_d: break
        divisor[ll].append(d)
        divisor[ll].append(inv_d)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)
        INF = float('inf')
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) enumerate all possible substrings, and pre-compute the (minimum) conversion
        # costs associated with each, by trying out all valid divisors
        # 2) solve by partition DP

        def make_sp_cost(substr: str, d: int) -> int:
            n = len(substr)
            m = n // d // 2
            c = 0
            # enumerate possible starting indices: overall O(n)
            for j in range(d):
                res = []
                for i in range(j, n, d):
                    res.append(substr[i])  
                # compute letter changes to make semi-palindrome
                for i in range(m):
                    if res[i] != res[-(i + 1)]:
                        c += 1
            return c

        conv_cost = [ [INF] * n for _ in range(n) ]
        # compute the letter costs to make semi-palindrome for all possible substrings
        for l in range(n):
            for r in range(l, n):
                substr = s[l : r + 1]
                for d in divisor[r - l + 1]:
                    conv_cost[l][r] = fmin(conv_cost[l][r], make_sp_cost(substr, d))

        # partition DP: achieve k substrings, each being a semi-palindrome
        @cache
        def f(l: int, r: int, p: int) -> int:
            if p > k:
                return INF
            if r == n - 1:
                return conv_cost[l][r] if p == k else INF
            # pruning: insufficient partitions left
            if n - r < k - p:
                return INF
            res = INF
            # skip
            res = fmin(res, f(l, r + 1, p))
            # take this as the end of a partition
            res = fmin(res, conv_cost[l][r] + f(r + 1, r + 1, p + 1))
            return res

        return f(0, 0, 1)

s, k = "abcac", 2
s, k = "abcdef", 2
s, k = "aabbaa", 3
s, k = "edaswf", 1

Solution().minimumChanges(s, k)