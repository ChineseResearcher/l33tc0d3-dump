# backtracking - medium
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # key ideas:
        # 1) sort the candidates and only keep candidates[i] <= target
        # 2) use a backtracking algorithm to pick indices

        candidates.sort()
        c = [x for x in candidates if x <= target]

        n = len(c)
        ans = []

        def f(i: int, seq: List[int], seqSum: int) -> None:

            nonlocal ans
            if seqSum > target:
                return

            if seqSum == target:
                ans.append(seq[:])

            for j in range(i, n):
                seq.append(c[j])
                seqSum += c[j]
                _ = f(j, seq, seqSum)
                seq.pop()
                seqSum -= c[j]

        _ = f(0, [], 0)
        return ans

candidates, target = [2], 1
candidates, target = [2,3,5], 8
candidates, target = [2,3,6,7], 7

Solution().combinationSum(candidates, target)