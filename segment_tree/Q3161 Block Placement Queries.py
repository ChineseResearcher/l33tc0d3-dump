# segment tree - hard
from typing import List
from sortedcontainers import SortedList
class SegTree:
    def __init__(self, n: int):

        # self.n is forced to be the smallest power of 2 that is strictly larger than n-1
        # this ensures that each leaf node occupies one index by creating self.n leaf nodes
        self.n = 1 << n.bit_length()
        self.tree = [0] * (2 * self.n)

    def update_recur(self, ind: int, val: int, node:int, start:int, end:int):
        # leaf node
        if start == end:
            self.tree[node] = val
            return
        
        mid = (start + end) // 2
        if ind <= mid:
            self.update_recur(ind, val, 2 * node + 1, start, mid)
        else:
            self.update_recur(ind, val, 2 * node + 2, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query_recur(self, ql: int, qr: int, node: int, start: int, end: int) -> int:
        if qr < start or ql > end:
            return float('-inf')

        if ql <= start and qr >= end:
            return self.tree[node]
        
        mid = (start + end) // 2
        l_max = self.query_recur(ql, qr, node * 2 + 1, start, mid)
        r_max = self.query_recur(ql, qr, node * 2 + 2, mid + 1, end)
        return max(l_max, r_max)

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
    
        # core ideas:
        # 1) use a sortedList to store the position of obstacles (axis)
        # 2) use a segment tree to store the max interval (free gap) for different ranges (itvl)

        axis = SortedList()
        # determine n 
        n = 3 * len(queries)
        n = min(n, max([q[1] for q in queries]))
        itvl = SegTree(n)

        # add a virtual obstacle at 0 so we can correctly 
        # update interval for the leftmost obstacle
        axis.add(0)

        ans = []
        for q in queries:

            if q[0] == 1:

                _, pos = q
                ind = axis.bisect(pos)

                # if there's an existing obstacle to the right
                if ind < len(axis):
                    
                    nxt = axis[ind]
                    itvl.update_recur(ind=nxt, val=nxt-pos, node=0, start=0, end=itvl.n-1)

                # for the existing obstacle to the left, update interval
                itvl.update_recur(ind=pos, val=pos - axis[ind-1], node=0, start=0, end=itvl.n-1)
                # add obstacle
                axis.add(pos)

            else:
                
                _, pos, block_len = q
                # locate the prev. obstacle
                prev = axis[axis.bisect(pos)-1]

                # we are accessing the max. interval that exists in range [0...prev]
                ranged_max = itvl.query_recur(ql=0, qr=prev, node=0, start=0, end=itvl.n-1)
                # if curr. queried position has no obstacle, then
                # the gap between prev and curr. position can also be considered
                max_itvl = max(ranged_max, pos - prev)

                ans.append(max_itvl >= block_len)

        return ans       
    
queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
queries = [[1,3],[2,3,1]]
queries = [[1,4],[2,11,11],[1,8],[2,4,4]]
queries = [[1,1],[1,5],[1,13],[1,14],[2,12,8]]
queries = [[1,11],[1,1],[1,12],[2,1,6],[2,11,4]]

Solution().getResults(queries)