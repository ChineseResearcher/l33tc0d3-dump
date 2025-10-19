# graph - medium
from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        n = len(s)
        # string in python is compared lexicographically 
        # so there's no need for us to convert number string to number

        # core ideas:
        # 1) model this problem as a graph problem and track the
        # lexicographically smallest number string ever formed

        # 2) init. the answer as the largest (lexi) number string possible
        # i.e. '9' * len(s)
        ans = '9' * n

        visited, q = set(((s),)), deque([s])
        while q:

            curr = q.popleft()
            if curr < ans:
                ans = curr

            # op1: add integer "a" to odd indices
            op1 = []
            for i in range(n):
                if i % 2 == 1:
                    op1.append(str((int(curr[i]) + a) % 10))
                else:
                    op1.append(curr[i])

            added = ''.join(op1)

            # op2: rotate right by "b" places
            rotated = curr[-b:] + curr[:(n-b)]

            if added not in visited:
                q.append(added)
                visited.add(added)

            if rotated not in visited:
                q.append(rotated)
                visited.add(rotated)

        return ans

s, a, b = "5525", 9, 2
s, a, b = "74", 5, 1
s, a, b = "0011", 4, 2

Solution().findLexSmallestString(s, a, b)