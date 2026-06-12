# two pointers - medium
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        # key ideas:
        # 1) match t as far as possible
        # 2) use two pointers

        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                j += 1
            i += 1

        return n - j
    
s, t = 'z', 'abcde'
s, t = 'abcde', 'a'
s, t = 'coaching', 'coding'

Solution().appendCharacters(s, t)