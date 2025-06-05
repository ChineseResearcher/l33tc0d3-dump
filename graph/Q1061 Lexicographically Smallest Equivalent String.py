# graph - medium
from string import ascii_lowercase as lwc
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        n = len(s1)
        # using the idea of Union Find, create a parent dict
        # initially, all 26 alphabets are its own parents
        p = {c:c for c in lwc}

        def find(c):
            # path-compression
            if p[c] != c:
                p[c] = find(p[c])
            return p[c]

        def union(x, y):

            rootX, rootY = find(x), find(y)
            if rootX < rootY:
                p[rootY] = rootX
            elif rootY < rootX:
                p[rootX] = rootY

        for i in range(n):
            c1, c2 = s1[i], s2[i]
            union(c1, c2)

        for c in lwc:
            # ensure all chars are compressed
            _ = find(c)

        # construct smallest string from baseStr
        ans = []
        for char in baseStr:
            ans.append(p[char])

        return ''.join(ans)
    
s1, s2, baseStr = "parker", "morris", "parser"
s1, s2, baseStr = "hello", "world", "hold"
s1, s2, baseStr = "leetcode", "programs", "sourcecode"

Solution().smallestEquivalentString(s1, s2, baseStr)