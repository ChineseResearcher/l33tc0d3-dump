# dp - hard
from functools import cache
class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:

        n = len(rods)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) meet-in-the-middle (because n // 2 <= 10) + DP
        # 2) f(i, w1, w2) gives us the set of possible diff from the rods' weights
        # and their corresponding max. weight of the 1st rod
        
        # helper to join dict
        def join(curr_dict: dict, new_dict: dict) -> dict:
            for d, v in new_dict.items():
                if d not in curr_dict:
                    curr_dict[d] = v
                else:
                    curr_dict[d] = fmax(curr_dict[d], v)
            return curr_dict

        @cache
        def f(i: int, w1: int, w2: int) -> dict:
            if i == T: 
                return {w1 - w2: w1}

            res = dict()
            # skip for both
            res = join(res, f(i + 1, w1, w2))
            # take (1): add to w1
            res = join(res, f(i + 1, w1 + rods[i], w2))
            # take (2): add to w2
            res = join(res, f(i + 1, w1, w2 + rods[i]))

            return res

        # i takes range [0, n // 2]
        T = m = n // 2 
        s1 = f(0, 0, 0)

        f.cache_clear()

        # i takes range [n // 2, n]
        T = n 
        s2 = f(m, 0, 0)

        # collect paired diffs and track best answers
        ans = 0
        for diff in s1.keys():
            if -diff in s2.keys():
                ans = fmax(ans, s1[diff] + s2[-diff])

        return ans

rods = [1,2]
rods = [1,2,3,6]
rods = [1,2,3,4,5,6]
rods = [1] * 20

Solution().tallestBillboard(rods)