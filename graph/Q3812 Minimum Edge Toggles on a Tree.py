# graph - hard
from typing import List
from collections import defaultdict
class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        
        # key idea:
        # Use post-order DFS to greedily flip edges from leaves up, 
        # ensuring each node matches the target before moving to its parent.

        # first convert to list of binary integers for start & target
        start = list(map(int, list(start)))
        target = list(map(int, list(target)))

        # create a counter to record the number of flips at each node
        flip_cnt = {i:0 for i in range(n)}

        # record the edge and its index in a dict
        edge_idx = dict()
        for idx, (u,v) in enumerate(edges):
            edge_idx[(u, v)] = idx
            edge_idx[(v, u)] = idx

        # build undirected tree
        tr = defaultdict(list)
        for u, v in edges:
            tr[u].append(v)
            tr[v].append(u)

        # collect flipped edge indices
        ans = set()

        def f(curr:int, prev:int) -> None:

            nonlocal ans
            # early return
            if -1 in ans:
                return

            for neighbour in tr[curr]:
                if neighbour != prev:
                    _ = f(neighbour, curr)

            # compute the final state after some flips
            if (start[curr] + flip_cnt[curr]) % 2 != target[curr]:
                flipped = (curr, prev)
                if flipped not in edge_idx:
                    ans.add(-1)
                else:
                    ans.add(edge_idx[flipped])
                    flip_cnt[curr] += 1
                    flip_cnt[prev] += 1

        # root at any node of the tree
        _ = f(0, -1)

        if -1 in ans: return [-1]
        return sorted(list(ans))
    
n, edges, start, target = 2, [[0,1]], "00", "01"
n, edges, start, target = 3, [[0,1],[1,2]], "010", "100"
n, edges, start, target = 7, [[0,1],[1,2],[2,3],[3,4],[3,5],[1,6]], "0011000", "0010001"

Solution().minimumFlips(n, edges, start, target)