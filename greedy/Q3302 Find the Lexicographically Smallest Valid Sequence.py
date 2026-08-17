# greedy - medium
from typing import List
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        n, m = len(word1), len(word2)
        # key ideas:
        # 1) this question can be solved more simply with Greedy + Suffix Preprocessing instead of DP
        # 2) we can perform suffix matching s.t. sf[i] records the longest matching
        # suffix of word2 using some subsequence from word1[i...n-1]
        # 3) when we iterate forward, the curr. index is taken as the "pivot", meaning
        # the 1 change is restricted to the pivot if two chars at pivot index in word1 and word2 differ
        # 4) the lexicographically smallest valid sequence involves the first such pivot
        # where prefix match cnt + 1 + suffix match cnt >= word2.length

        sf = [0] * n
        # two-pointer to match word2
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                sf[i] += 1
                j -= 1

            if i < n - 1:
                sf[i] += sf[i + 1]

        pfc, j, p, changed = 0, 0, -1, False
        for i in range(n):

            # get suffix match cnt
            sfc = sf[i + 1] if i + 1 < n else 0

            # note: there's a tricky part here, if the pivot i matches
            # with word2[j], then the change is allowed to happen in [0..i] or [i+1..n-1]
            # we will need to track a boolean so as to use the change as early as possible 
            if pfc + 1 + sfc >= m:
                if word1[i] != word2[j]: changed = True
                p = i
                break

            # prefix matching
            if j < m and word1[i] == word2[j]:
                pfc += 1
                j += 1

        if p == -1: return []

        # collect best seq. based on pivot
        pfi, j = [], 0
        for i in range(p):
            if j == m: break

            if word1[i] == word2[j]:
                pfi.append(i)
                j += 1
            else:
                if not changed:
                    pfi.append(i)
                    j += 1
                    changed = True

        sfi, j = [], len(pfi) + 1
        for i in range(p + 1, n):
            if j == m: break

            if word1[i] == word2[j]:
                sfi.append(i)
                j += 1
            else:
                if not changed:
                    sfi.append(i)
                    j += 1
                    changed = True

        return pfi + [p] + sfi

word1, word2 = "abc", "ab"
word1, word2 = "bacdc", "abc"
word1, word2 = "vbcca", "abc"
word1, word2 = "ccbccccbcc", "b"
word1, word2 = "ghhgghhhhhh", "gg"

Solution().validSequence(word1, word2)