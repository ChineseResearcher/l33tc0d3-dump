# dp - hard
class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        
        def f(pos:int, tight:int, atOdd:int, started:int, diff:int) -> int:

            # "atOdd" indicates whether we are at the odd index of 
            # the "actual" sequence that we are forming

            # capture the diff between odd and even digit sum as "diff"

            if pos == N:
                return 1 if (diff == 0 and started) else 0
            
            # prune when rest of all digits remaining * 9 would not balance the diff
            if diff > (N-pos) * 9:
                return 0
            
            # cache was TLE-ed, had to enforce look-up table
            if dp[pos][tight][atOdd][started][diff+72] != -1:
                return dp[pos][tight][atOdd][started][diff+72]
            
            ub = digits[pos] if tight == 1 else 9
            
            res = 0
            for i in range(ub+1):

                n_diff = diff
                # update diff according to atOdd flag
                if atOdd:
                    n_diff += i
                else:
                    n_diff -= i

                n_started = 1 if (started == 1 or i > 0) else 0
                n_tight = 1 if (tight == 1 and i == ub) else 0

                res += f(pos + 1,
                        n_tight,
                        # only start inverting the flag when seq. has started
                        1 - atOdd if n_started == 1 else atOdd,
                        n_started, 
                        n_diff)

            dp[pos][tight][atOdd][started][diff+72] = res
            return res

        def set_dp_table(n):
            DIFF_SIZE = 145   # [-72, +72]

            dp = [[[[[-1 for _ in range(DIFF_SIZE)]
                    for _ in range(2)]
                    for _ in range(2)]
                    for _ in range(2)]
                    for _ in range(n)]
            
            return dp

        # solve up to high
        digits = list(map(int, str(high)))
        N = len(digits)
        dp = set_dp_table(N)
        h = f(0, True, True, False, 0)

        # solve up to low-1
        digits = list(map(int, str(low-1)))
        N = len(digits)
        dp = set_dp_table(N)
        l = f(0, True, True, False, 0)

        return h-l

low, high = 1, 100
low, high = 120, 129
low, high = 1234, 1234
low, high = 1, int(1e15)
low, high = 591973437298872, 600363113877048
low, high = 511884044927731, 934167144428228
low, high = 743096236904626, 974625443790444

Solution().countBalanced(low, high)