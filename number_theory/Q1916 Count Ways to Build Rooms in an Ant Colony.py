# number theory - hard
MOD, maxN = int(1e9 + 7), int(1e5)
# pre-computation of inverse factorials for fast multinomial coeff. compute
fact = [1] * (maxN + 1)
for i in range(1, maxN + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact = [1] * (maxN + 1)
inv_fact[maxN] = pow(fact[maxN], MOD - 2, MOD)
for i in range(maxN, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

from collections import defaultdict
class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:

        n = len(prevRoom)
        # key ideas:
        # 1) first build the tree structure using given array
        # 2) run a DFS down the tree to collect answer with combinatorics
        tr = defaultdict(list)

        for i in range(n):
            tr[prevRoom[i]].append(i)

        def f(curr: int) -> tuple[int, int]:

            if not tr[curr]:
                return (1, 1)

            res, tot_cnt, inv_fac_prod = 1, 0, 1
            for child in tr[curr]:
                n_res, n_cnt = f(child)
                res *= n_res 
                inv_fac_prod *= inv_fact[n_cnt]
                inv_fac_prod %= MOD
                tot_cnt += n_cnt

            mtn_coeff = fact[tot_cnt] * inv_fac_prod
            res *= mtn_coeff
            res %= MOD
            return (res, tot_cnt + 1)

        ans, _ = f(-1)
        return ans

prevRoom = [-1,0,1]
prevRoom = [-1,0,0,1,2]

Solution().waysToBuildRooms(prevRoom)