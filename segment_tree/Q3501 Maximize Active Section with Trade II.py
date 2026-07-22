# segment tree - hard
from typing import List
from bisect import bisect_right, bisect_left
fmax = lambda a, b: a if a > b else b
class MaxSegTree:
    def __init__(self, arr):
        n = len(arr)

        self.size = 1
        while self.size < n:
            self.size <<= 1

        self.st = [0] * (2 * self.size)

        for i, v in enumerate(arr):
            self.st[self.size + i] = v

        for i in range(self.size - 1, 0, -1):
            self.st[i] = fmax(self.st[i << 1], self.st[i << 1 | 1])

    def query(self, l, r):
        if l > r:
            return 0

        l += self.size
        r += self.size

        ans = 0
        while l <= r:

            if l & 1:
                ans = fmax(ans, self.st[l])
                l += 1

            if not (r & 1):
                ans = fmax(ans, self.st[r])
                r -= 1

            l >>= 1
            r >>= 1

        return ans

class MergeZeroBlocksSolver:
    def __init__(self, s, seg):
        self.s = s
        self.seg = seg

        # segment boundaries
        self.seg_starts = []
        for start, typ, length in seg:
            self.seg_starts.append(start)

        # extract zero-blocks
        self.zeros = []
        for seg_id, (start, typ, length) in enumerate(seg):
            if typ == 0:
                self.zeros.append({
                    "seg_id": seg_id,
                    "start": start,
                    "end": start + length - 1,
                    "length": length
                })

        # map: segment id -> zero index
        self.seg_to_zero = {}
        for zi, z in enumerate(self.zeros):
            self.seg_to_zero[z["seg_id"]] = zi

        # pair sums of consecutive 0-blocks
        pair_sum = []
        for i in range(len(self.zeros) - 1):
            pair_sum.append(self.zeros[i]["length"] + self.zeros[i + 1]["length"])
        
        # build RMQ segment tree based on pairSum(s)
        self.segtree = MaxSegTree(pair_sum)

    # locate segment containing position
    def find_segment(self, pos):
        return bisect_right(self.seg_starts, pos) - 1

    def query(self, l, r):

        best_pair = 0
        left_seg, right_seg = self.find_segment(l), self.find_segment(r)

        ls, ltyp, llen = self.seg[left_seg]
        rs, rtyp, rlen = self.seg[right_seg]

        if (left_seg != right_seg and (not ltyp or not rtyp) and (l > ls or r < rs + rlen - 1)):

            zl = self.seg_to_zero[left_seg] if not ltyp else -1
            zr = self.seg_to_zero[right_seg] if not rtyp else -1

            # special case:
            # left-cut 0-block and right-cut 0-block form one pair
            if zr == zl + 1 > 0:
                usable_left = ls + llen - l
                usable_right = r - rs + 1
                best_pair = fmax(best_pair, usable_left + usable_right)

            else:
                # left-cut candidate
                if not ltyp and l > ls:
                    if zl + 1 < len(self.zeros):
                        next_zero = self.zeros[zl + 1]
                        if next_zero["start"] <= r:
                            usable_left = ls + llen - l
                            best_pair = fmax(best_pair, usable_left + next_zero["length"])

                # right-cut candidate
                if not rtyp and r < rs + rlen - 1:
                    if zr - 1 >= 0:
                        prev_zero = self.zeros[zr - 1]
                        if prev_zero["end"] >= l:
                            usable_right = r - rs + 1
                            best_pair = fmax(best_pair, prev_zero["length"] + usable_right)

        # fully-covered interior zeros
        first_zero = bisect_left(self.zeros, l, key=lambda z: z["start"])
        last_zero = bisect_right(self.zeros, r, key=lambda z: z["end"]) - 1

        # if we have valid interior adjacent 0-pairs, query for max. pairSum in range [l, r]
        if last_zero - first_zero >= 1:
            best_pair = fmax(best_pair, self.segtree.query(first_zero, last_zero - 1))

        return best_pair

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        # init. an array "seg" to store <starting idex, type of segment (0/1), length>
        seg = []

        ones = s.count("1")

        # compress original string into 0/1-blocks
        prev_i, prev = 0, int(s[0])
        for i in range(1, n):
            curr = int(s[i])
            if curr != prev:
                seg.append((prev_i, prev, i - prev_i))
                prev, prev_i = curr, i

        # collect last block
        seg.append((prev_i, prev, n - prev_i)) 

        solver = MergeZeroBlocksSolver(s, seg)

        ans = []
        for l, r in queries:
            ans.append(solver.query(l, r) + ones) 

        return ans

s, queries = "01", [[0,1]]
s, queries = "1100", [[3,3],[1,2]]
s, queries = "01010", [[0,3],[1,4],[1,3]]
s, queries = "1000100", [[1,5],[0,6],[0,4]]
s, queries = "0100", [[0,3],[0,2],[1,3],[2,3]]
s, queries = "0001000000", [[2,7],[8,9],[2,6],[8,8],[6,9]]
s, queries = "110000101001", [[7,8],[2,5],[2,11],[4,10],[3,9],[6,8],[5,8]]

Solution().maxActiveSectionsAfterTrade(s, queries)