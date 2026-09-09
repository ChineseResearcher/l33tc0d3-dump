# dp - hard
import bisect
from typing import List
from collections import defaultdict
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # key ideas:
        # 1) pick / no-pick DP with binary search lookup for previous largest smaller index
        # 2) sort intervals by right end
        # 3) pre-process intervals s.t. for each distinct interval, we only keep the
        # one w/ the largest weight

        f_intervals, intvl_max_w, intvl_idx = [], defaultdict(int), defaultdict(int)
        for i in range(len(intervals)):
            l, r, w = intervals[i]
            if w > intvl_max_w[(l, r)]:
                intvl_max_w[(l, r)] = w
                intvl_idx[(l, r)] = i

        for l, r in intvl_max_w.keys():
            f_intervals.append((l, r, intvl_max_w[(l, r)]))

        n = len(f_intervals)
        # build dp[k][r], storing a list of indices indicating the k chosen indices
        # for considering up to f_intervals[:r]
        dp = [ [[] for _ in range(n)] for _ in range(4) ]

        f_intervals.sort(key=lambda x: x[1])

        # helper to compare total weight of two lists of chosen indices
        def max_w(p1:List[int], p2:List[int]) -> List[int]:
            w1, w2 = 0, 0
            p1.sort()
            p2.sort()
            # p2 (pick) is invalid
            if p2[0] == -1:
                return p1

            for i in p1:
                w1 += intervals[i][2]
            for i in p2:
                w2 += intervals[i][2]
            if w1 > w2:
                return p1
            elif w2 > w1:
                return p2
            else:
                return min(p1, p2)

        dp[0][0].append(intvl_idx[(f_intervals[0][0], f_intervals[0][1])])
        # track largest weight, and lexicographically smallest indicess
        b_score, b_i = f_intervals[0][2], dp[0][0]
        for i in range(1, n):
            for k in range(min(i + 1, 4)):

                skip = dp[k][i - 1]

                cl, cr = f_intervals[i][0], f_intervals[i][1]
                if k == 0:
                    pick = [intvl_idx[(cl, cr)]]
                else:
                    pick = [-1] * (k + 1)
                    # override pick if there is a valid smaller index
                    j = bisect.bisect_left(f_intervals, cl, key=lambda x: x[1]) - 1
                    if j >= 0:
                        pick = dp[k - 1][j] + [intvl_idx[(cl, cr)]]

                # evaluate both options using helper
                dp[k][i] = max_w(skip, pick)

        # track best selection of indices b_i
        for k in range(4):  
            c_score = 0
            for pi in dp[k][n - 1]:
                c_score += intervals[pi][2]
                
            if c_score > b_score:
                b_i = dp[k][n - 1]
                b_score = c_score
            elif c_score == b_score:
                b_i = min(b_i, dp[k][n - 1])

        return b_i

intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
intervals = [[17,17,10],[23,23,23],[3,8,31],[17,21,48],[18,24,44]]
intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Solution().maximumWeight(intervals)