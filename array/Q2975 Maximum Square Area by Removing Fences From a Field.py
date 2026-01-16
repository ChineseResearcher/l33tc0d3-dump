# array - medium
from typing import List
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        # key ideas:
        # 1) enumerate all possible interval pairs row-wise / col-wise

        # 2) this would give us all the possibilities of side lengths,
        # and we store row-wise / col-wise results separately in two hashsets

        # 3) largest square is then the largest common side length present in both

        # helper to generate unique intervals
        def get_intvl(fences: List[int]) -> set:

            res = set()
            for i in range(len(fences)-1):
                for j in range(i+1, len(fences)):
                    res.add(fences[j]-fences[i])
            return res

        # sort the horizontal fences, and append start/end
        hFences.sort()
        hf = [1]
        hf.extend(hFences)
        hf.append(m)
        h_intvl = get_intvl(hf)

        # do the same thing for vertical fences
        vFences.sort()
        vf = [1]
        vf.extend(vFences)
        vf.append(n)
        v_intvl = get_intvl(vf)

        common = h_intvl & v_intvl
        if not common: return -1
        return pow(max(common), 2) % int(1e9 + 7)

m, n, hFences, vFences = 4, 3, [2,3], [2]
m, n, hFences, vFences = 6, 7, [2], [4]

Solution().maximizeSquareArea(m, n, hFences, vFences)