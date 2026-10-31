# sliding window - medium
from collections import defaultdict
class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:

        # key ideas:
        # 1) sorting + sliding window
        # 2) record servers with requests coming in at every distinct timestamp
        # 3) sort distinct timestamps from (2), and also sort queries, then slide window over it
        c = defaultdict(list)

        for mx, t in logs:
            c[t].append(mx)

        ts = sorted(c.keys())
        m = len(ts)

        l, r, activeCnt, ans = 0, 0, dict(), dict()
        for rb in sorted(queries):
            # add all active requests
            while r < m and ts[r] <= rb:
                for mx in c[ts[r]]:
                    if mx not in activeCnt:
                        activeCnt[mx] = 0
                    activeCnt[mx] += 1
                r += 1
            # drop all expired requests
            lb = rb - x
            while l < r and ts[l] < lb:
                for mx in c[ts[l]]:
                    activeCnt[mx] -= 1
                    if activeCnt[mx] == 0:
                        del activeCnt[mx]
                l += 1
            ans[rb] = n - len(activeCnt)

        return [ans[q] for q in queries]

n, logs, x, queries = 3, [[1,32],[1,35]], 8, [38]
n, logs, x, queries = 3, [[1,3],[2,6],[1,5]], 5, [10,11]
n, logs, x, queries = 6, [[1,21]], 10, [24,35,28,26,20,25,16,31,12]

Solution().countServers(n, logs, x, queries)