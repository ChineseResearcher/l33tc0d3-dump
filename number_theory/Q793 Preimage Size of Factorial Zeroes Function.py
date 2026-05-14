# number theory - hard
class Solution:
    def preimageSizeFZF(self, k: int) -> int:

        if k == 0: return 5 # 0!, 1!, 2!, 3!, 4!

        k_rem = k
        # we can observe that:
        # 1) to obtain a trailing '0' we need a pair of (2, 5) in the factors
        # e.g. 30 = 2 * 5 * 3, where 1 pair of (2, 5) exists

        # 2) only count of 5 in factors is the limiting factor as the count of 
        # 2 grows much faster than 5
        
        # 3) for below non-overlapping ranges, we observe the count of 5
        # contributed by each range
        # [0, 5] -> 1
        # (5, 25] -> 5
        # (25, 125] -> 25
        # (125, 625] -> 125
        # (625, 3125] -> 625
        # There is a geometric relationship here:
        # If we search up to number 5^p, we obtain count of 5 equal to sum of 
        # geometric series 5^0 + 5^1 + 5^2 + .... + 5^(p-1)

        # 4) we need to further apply bianry search if k is not a sum of geometric series
        p = 1
        while True:
            k_rem -= pow(5, p-1)
            if k_rem - pow(5, p) < 0:
                break
            p += 1

        # a perfect sum of geometric series
        if k_rem == 0: return 5

        # binary search on range [5^p + 1, 5^(p+1)]
        l, r = pow(5, p) + 1, pow(5, p + 1)
        fac = [pow(5, i) for i in range(1, p+2)]

        ans = 0
        while l <= r:

            mid = (l + r) // 2

            cnt_5 = 0
            for f in fac:
                cnt_5 += mid // f

            # found the number in range [l, r] with
            # k occurrences of 5 in its factors
            if cnt_5 == k:
                ans = 5
                break
            elif cnt_5 > k:
                r = mid - 1
            elif cnt_5 < k:
                l = mid + 1

        return ans

k = 0
k = 3
k = 5
k = int(1e9)

Solution().preimageSizeFZF(k)