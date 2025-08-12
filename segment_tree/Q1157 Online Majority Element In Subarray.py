# segment tree - hard
from typing import List
from collections import defaultdict
import bisect
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [[None,None] for _ in range(4 * self.n)]
        self.build(data, 0, 0, self.n-1)

    def merge_vote(self, maj1, cnt1, maj2, cnt2):
        # Boyer-Moore voting
        # key property: vote(arr1 + arr2) = vote(arr1) (x) vote(arr2)
        # where "(x)" denotes a merge operation
        if maj1 == maj2:
            maj_curr, cnt_curr = maj1, cnt1 + cnt2
        else:
            if cnt1 >= cnt2:
                maj_curr, cnt_curr = maj1, cnt1 - cnt2
            else:
                maj_curr, cnt_curr = maj2, cnt2 - cnt1

        return (maj_curr, cnt_curr)
    
    def build(self, data, node, start, end):
        if start == end:
            # leaf node will have a majority element w/ count 1
            self.tree[node][0] = data[start]
            self.tree[node][1] = 1
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)

            # assign curr. node val
            maj1, cnt1 = self.tree[2 * node + 1]
            maj2, cnt2 = self.tree[2 * node + 2]
            maj_curr, cnt_curr = self.merge_vote(maj1, cnt1, maj2, cnt2)
            # fill curr. node w/ merged voting result
            self.tree[node] = [maj_curr, cnt_curr]

    def query(self, ql, qr, node, start, end):
        if qr < start or ql > end:
            return (-1,0)
        
        if ql <= start and qr >= end:
            return (self.tree[node][0], self.tree[node][1])
        
        mid = (start + end) // 2
        maj1, cnt1 = self.query(ql, qr, node * 2 + 1, start, mid)
        maj2, cnt2 = self.query(ql, qr, node * 2 + 2, mid + 1, end)
        # return merged voting result
        return self.merge_vote(maj1, cnt1, maj2, cnt2)

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.itvl = SegmentTree(arr)
        self.num_indices = defaultdict(list)
        # build the appearing index for each number in order
        for idx, x in enumerate(arr):
            self.num_indices[x].append(idx)

    def query(self, left: int, right: int, threshold: int) -> int:

        # get the majority element "k" in range [left, right]
        # note that the voting count is not needed and ignored
        k, _ = self.itvl.query(left, right, 0, 0, self.itvl.n-1)
        if k == -1:
            return -1

        # for majority element k ,we need to verify if it 
        # satisfies the threshold frequency over range [left, right]
        s = bisect.bisect_left(self.num_indices[k], left)
        e = bisect.bisect_right(self.num_indices[k], right)

        return k if e - s >= threshold else -1
    
arr = [1, 1, 2, 2, 1, 1]
obj = MajorityChecker(arr)

commands = ["query", "query", "query"]
arguments = [[0,5,4], [0,3,3], [2,3,2]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))