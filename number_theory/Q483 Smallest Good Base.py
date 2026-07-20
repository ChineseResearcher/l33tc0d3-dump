# number theory - hard
class Solution:
    def smallestGoodBase(self, n: str) -> str:

        n = int(n)
        # key ideas:
        # 1) suppose for a given bit length, we want to guess the base k
        # s.t. pow(k, 0) + pow(k, 1) + ... + pow(k, bit_length) = n exactly,
        # the sum result is monotonic w.r.t to k, hence we use binary search
        # to find if such k exists
        # 2) explore all possible bit lengths, and track the smallest good base

        def bs(bit_length: int) -> int:

            l, r = 2, n
            # binary search on the base
            while l <= r:

                mid = (l + r) >> 1
                # sum of geometric series:
                # rewrite pow(k, 0) + pow(k, 1) + ... + pow(k, b) as,
                # S = (k^(b + 1) - 1) / (k - 1)
                S = (pow(mid, bit_length) - 1) // (mid - 1)
                if S == n:
                    return mid
                elif S > n:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1

        # determine the bit_length we explore up to
        # using smallest base assumption, i.e. k = 2
        currSum, pos = 0, 0
        while currSum < n:
            currSum += pow(2, pos)
            pos += 1

        ans = n + 1
        for b in range(1, pos + 1):
            res = bs(b)
            if res != -1:
                ans = min(ans, bs(b))

        return str(ans)

n = "13"
n = "4681"
n = "1000000000000000000"

Solution().smallestGoodBase(n)