# number theory - medium
from typing import List
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        MOD = int(1e9 + 7)
        # key ideas:
        # 1) take s = "123456789" for example
        # substring s[3...7] = 45678
        # and it is equivalent to 12345678 - 12300000 = 12345678 - 123 * pow(10, 7-3+1)

        # 2) since the question wants to query answer to be modulo over MOD
        # the same expression can be re-formulated as:
        # [ (12345678 % MOD) - ((123 % MOD) * (pow(10, 7-3+1) % MOD)) % MOD ] % MOD

        # 3) then it boils down to pre-computing prefix modulo results
        # in this case, we need to access (12345678 % MOD) and (123 % MOD) when querying

        # 4) how can we pre-compute the modulo results efficiently?
        # let r = k % MOD
        # for a new digit d, we obtain the new prefix number as k + 10 + d
        # then if we calculate the modulo, it can be simplified as
        # (k * 10 + d) % MOD = ( ((k % MOD) * (10 % MOD)) % MOD + (d % MOD) ) % MOD
        #                    = ( (r * 10) % MOD + d ) % MOD

        pf_mod, pf_sum, pf_cnt = [int(s[0])], [int(s[0])], [min(int(s[0]), 1)]
        for i in range(1, n):
            d, r, c = int(s[i]), pf_mod[i-1], pf_cnt[i-1]
            if d > 0:
                r = ((r * 10) % MOD + d) % MOD
                c = c + 1
            
            pf_mod.append(r)
            pf_cnt.append(c)

            pf_sum.append(pf_sum[i-1] + d)

        ans = []
        for l, r in queries:
            
            dSum = pf_sum[r] - (pf_sum[l-1] if l-1 >= 0 else 0)
            rangeCnt = pf_cnt[r] - (pf_cnt[l-1] if l-1 >= 0 else 0)
            diff = pf_mod[r] - (pf_mod[l-1] if l-1 >= 0 else 0) * pow(10, rangeCnt, MOD)
            ans.append((diff * dSum) % MOD)

        return ans

s, queries = "1000", [[0,3],[1,1]]
s, queries = "9876543210", [[0,9]]
s, queries = "10203004", [[0,7],[1,3],[4,6]]

Solution().sumAndMultiply(s, queries)