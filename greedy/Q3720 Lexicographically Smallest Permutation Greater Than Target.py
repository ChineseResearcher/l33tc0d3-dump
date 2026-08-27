# greedy - medium
from collections import Counter
from string import ascii_lowercase as L
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        n = len(s)
        # key ideas:
        # 1) enumeration + greedy assignment
        # 2) we can enumerate up to target[:k] as the unchanged prefix, and modify
        # s[k] to be next strictly larger char. 
        # 3) we need to pre-compute k by comparing between target string, and
        # char. frequencies of s

        # helper to find the next available larger char.
        def nextChar(char:str, freq:Counter) -> str:
            if char == 'z': return ''
            currO = ord(char) + 1 - ord('a')
            while currO < 26:
                if freq[L[currO]] > 0:
                    return L[currO]
                currO += 1

            return ''

        c = Counter(s)

        k, cc = -1, c.copy()
        for i in range(n):
            if cc[target[i]] == 0:
                break
            cc[target[i]] -= 1
            k = i

        ans = ''
        for p in range(-1, k + 1):
            cc = c.copy()
            # fix target[:p+1] as part of the final permutation
            for i in range(p + 1):
                cc[target[i]] -= 1

            # modify char. at p + 1
            if p + 1 == n:
                break
            nc = nextChar(target[p + 1], cc)
            if not nc:
                continue
            cc[nc] -= 1

            prefix = target[:p + 1]
            suffix = ''.join([char * cc[char] for char in sorted(cc.keys())])
            ans = prefix + nc + suffix

        return ans

s, target = "abc", "bba"
s, target = "leet", "code"
s, target = "baba", "bbaa"

Solution().lexGreaterPermutation(s, target)