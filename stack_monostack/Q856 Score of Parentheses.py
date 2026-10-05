# stack - medium
from collections import defaultdict
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        # key ideas:
        # 1) given string is already VPS, we just need to tabulate score
        # 2) use a dictionary of stacks representing the scores attained at each nesting depth
        score = defaultdict(list)
        
        depth = 0
        for x in s:
            if x == '(':
                depth += 1
            else:
                if score[depth]:
                    score[depth - 1].append(sum(score[depth]) * 2)
                    score[depth].clear()
                else:
                    score[depth - 1].append(1)
                depth -= 1

        return sum(score[0])

s = "()"
s = "(())"
s = "()()"
s = "(()(()))"

Solution().scoreOfParentheses(s)