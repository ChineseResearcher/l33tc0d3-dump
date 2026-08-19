# binary search tree - hard
from typing import List
from sortedcontainers import SortedList
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        
        n = len(s)
        # key ideas:
        # 1) ordered set + interval simulation
        # 2) simulation involves replacement / creation / merging of intervals

        intvl, ilen, iid = SortedList(), SortedList(), 0
        # process the string first to init. both ordered sets
        intvl.add((0, s[0], iid))
        iid += 1

        for i in range(1, n):
            if s[i] != s[i - 1]:
                intvl.add((i, s[i], iid))
                iid += 1

        for i in range(len(intvl) - 1):
            ilen.add((intvl[i + 1][0] - intvl[i][0], intvl[i][2]))
        ilen.add((n - intvl[-1][0], intvl[-1][2]))

        ans = []
        for i, qi in enumerate(queryIndices):
            c = queryCharacters[i]
            # use binary search to find the interval [L, R] that qi belongs to
            j = intvl.bisect_left((qi, '', -1))
            if j == len(intvl) or intvl[j][0] > qi:
                j -= 1

            L, cchar, cid = intvl[j]
            # no interval changes if char. is the same
            if cchar == c:
                ans.append(ilen[-1][0]) 
                continue

            R = (intvl[j + 1][0] - 1 if j + 1 < len(intvl) else n - 1)
            cLen = R - L + 1
            # discard curr. interval
            intvl.discard((L, cchar, cid))
            ilen.discard((cLen, cid))
            
            # insert new intervals: [L...qi - 1], [qi...qi], [qi + 1...R] if applicable
            if qi - 1 >= L:
                intvl.add((L, cchar, iid))
                ilen.add((qi - L, iid))
                iid + 1
            intvl.add((qi, c, iid))
            ilen.add((1, iid))
            iid += 1
            if R >= qi + 1:
                intvl.add((qi + 1, cchar, iid))
                ilen.add((R - qi, iid))
                iid += 1

            # merge interval [qi...qi] w/ left and / or right interval if applicable
            nj = intvl.bisect_left((qi, '', -1))
            cid = intvl[nj][2]
            nL, nR = qi, qi

            t1, t2 = None, None
            if nj - 1 >= 0 and intvl[nj - 1][1] == c:
                nL, _, nid = intvl[nj - 1]
                t1, t2 = intvl[nj - 1], (qi - nL, nid)

            t3, t4 = None, None
            if nj + 1 < len(intvl) and intvl[nj + 1][1] == c:
                nR = (intvl[nj + 2][0] - 1 if nj + 2 < len(intvl) else n - 1)
                _, _, nid = intvl[nj + 1]
                t3, t4 = intvl[nj + 1], (nR - qi, nid)

            if nR > nL:
                # remove merged left / right inteval if any
                if t1:
                    intvl.discard(t1)
                    ilen.discard(t2)
                if t3:
                    intvl.discard(t3)
                    ilen.discard(t4)
                # remove [qi...qi]
                intvl.discard((qi, c, cid))
                ilen.discard((1, cid))
                # insert new interval
                intvl.add((nL, c, iid))
                ilen.add((nR - nL + 1, iid))
                iid += 1
            
            ans.append(ilen[-1][0])

        return ans

s, queryCharacters, queryIndices = "abyzz", "aa", [2,1]
s, queryCharacters, queryIndices = "babacc", "bcb", [1,3,3]
s, queryCharacters, queryIndices = "exjwgrh", "qreuu", [5,4,0,1,5]

Solution().longestRepeating(s, queryCharacters, queryIndices)