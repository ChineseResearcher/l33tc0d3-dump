# dp - hard
from typing import List
from functools import cache
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:

        n = len(arr)
        # key ideas:
        # 1) odd-/even-numbered jumps require information on next smallest greater / greatest smaller
        # 2) for odd moves, we can sort the arr by (val ASC, idx ASC), and use monotonic stack to record
        # the next-to-jump information, similarly for even moves, we sort by (val DESC, idx ASC)
        # 3) solve DP problem with state (index, isOdd)

        T1 = sorted([(val, idx) for idx, val in enumerate(arr)])
        nG, st = [-1] * n, []
        for v, i in T1:
            while st and i > st[-1]:
                nG[st.pop()] = i
            st.append(i)

        T2 = sorted([(-val, idx) for idx, val in enumerate(arr)])
        nS, st = [-1] * n, []
        for v, i in T2:
            while st and i > st[-1]:
                nS[st.pop()] = i
            st.append(i)

        @cache
        def f(i:int, isOdd:bool) -> bool:

            if i == n-1: return True

            # odd jump -> next greater
            if isOdd: 
                if nG[i] != -1 and f(nG[i], not isOdd):
                    return True
            # even jump -> next smaller
            else:
                if nS[i] != -1 and f(nS[i], not isOdd):
                    return True
            
            return False

        ans = 0
        for i in range(n):
            if f(i, True): ans += 1

        return ans

arr = [5,1,3,4,2]
arr = [2,3,1,1,4]
arr = [10,13,12,14,15]
arr = [1,2,3,2,1,4,4,5]

Solution().oddEvenJumps(arr)