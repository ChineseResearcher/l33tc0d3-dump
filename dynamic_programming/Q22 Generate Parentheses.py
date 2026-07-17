# dp - medium
from typing import List
from functools import cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # key ideas:
        # 1) generate valid parenthesis combinations using recursive decomposition
        # 2) DP is applicable here because we are trying all splits on curr. n
        # which creates overlapping subproblems
        # 3) special case on i = 1 where we have the extra option to add enclosing
        # bracket on every f(n - i) candidate

        @cache
        def f(n: int) -> set:

            if n == 1: return {'()'}

            res = set()
            for i in range(1, (n // 2) + 1):
                s1, s2 = f(i), f(n - i)
                if i == 1:
                    for y in s2:
                        res.add('()' + y)
                        res.add('(' + y + ')') # enclose
                        res.add(y + '()')
                else:
                    for x in s1:
                        for y in s2:
                            res.add(x + y)
                            res.add(y + x)

            return res

        return list(f(n))

n = 1
n = 3
n = 4

Solution().generateParenthesis(n)