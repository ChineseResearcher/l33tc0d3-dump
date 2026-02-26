# graph - hard
from collections import deque
from sortedcontainers import SortedSet
class Solution:
    def minOperations(self, s: str, k: int) -> int:

        n = len(s)
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) model this as a graph problem, where each graph node is represented
        # by the number of zeroes we have in the curr. binary string

        # 2) the optimal (mininum) answer is obtained when we first hit z = 0

        # 3) we need to prune our BFS based on ordered set & parity

        z = s.count("0")

        e_state = SortedSet([i for i in range(0, n+1, 2)])
        o_state = SortedSet([i for i in range(1, n+1, 2)])

        if z % 2 == 0:
            e_state.discard(z)
        else:
            o_state.discard(z)

        q = deque([(z,0)])
        while q:

            z, moves = q.popleft()
            if z == 0:
                return moves
                
            # at least choose max(0, k - (n - z)) "0"s
            min_pick = fmax(0, k - (n - z))
            # at most choose min(k, z) "0"s
            max_pick = fmin(k, z)

            # derive the range of new states on zeroes using max / min pick
            l, r = z + k - 2 * max_pick, z + k - 2 * min_pick
            
            # determine which unvisited states to process depending on parity
            if l % 2 == 0:
                ql, qr = e_state.bisect_left(l), e_state.bisect_right(r)
                cnt = qr - ql
                while cnt > 0:
                    nz = e_state[ql]
                    q.append((nz, moves + 1))
                    # new z state considered, so discard from unvisited states
                    e_state.discard(nz)
                    cnt -= 1

            else:
                ql, qr = o_state.bisect_left(l), o_state.bisect_right(r)
                cnt = qr - ql
                while cnt > 0:
                    nz = o_state[ql]
                    q.append((nz, moves + 1))
                    o_state.discard(nz)
                    cnt -= 1

        return -1

s, k = "1", 1
s, k = "110", 1
s, k = "101", 2
s, k = "0101", 3
s, k = "110010", 5
s, k = "1101101", 6
s, k = "0000", 3

Solution().minOperations(s, k)