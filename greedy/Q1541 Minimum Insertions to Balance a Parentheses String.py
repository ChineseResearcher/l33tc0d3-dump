# greedy - medium
class Solution:
    def minInsertions(self, s: str) -> int:

        n = len(s)
        # key ideas:
        # 1) "o" tracks the unclosed open brackets, "c" tracks the unused close brackets
        # 2) use close brackets greedily in multiples of 2, otherwise if there is only
        # 1 left, will need to make up another close bracket

        o, c, ans = 0, 0, 0  
        for i in range(n):
            x = s[i]
            if x == ')':
                c += 1
                # collapse "))" into ")"
                if c == 2:
                    if o > 0:
                        o -= 1
                    else:
                        ans += 1
                elif c == 1:
                    # locate odd ")" at the end of a consecutive ")" block
                    if (i + 1 == n or s[i + 1] == '('):
                        if o > 0:
                            o -= 1
                            ans += 1
                        else:
                            ans += 2
                        c = 0
                c %= 2
            else:
                o += 1

        ans += o * 2
        return ans

s = "())"
s = "(()))"
s = "))())("

Solution().minInsertions(s)