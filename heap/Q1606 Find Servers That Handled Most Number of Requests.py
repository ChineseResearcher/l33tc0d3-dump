# heap - hard
import heapq
from collections import Counter
from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        n = len(arrival)
        # key ideas:
        # 1) use minheap to store the servers in-use, in the format <avail_time, server_id>
        # 2) use ordered set to denote the free servers
        # 3) perform the simulation of algo mentioned, and tabulate assignment count to each server
        cnt = Counter()
        free = SortedList([x for x in range(k)])
        busy = []

        for i in range(n):
            # update free servers
            while busy and busy[0][0] <= arrival[i]:
                _, sid = heapq.heappop(busy)
                free.add(sid)

            m = len(free)
            if m > 0:
                # locate next available server
                j = free.bisect_left(i % k) % m
                ns = free[j]
                # enlist this server
                heapq.heappush(busy, (arrival[i] + load[i], ns))
                # mark as not free
                free.discard(ns)
                # final answer accounting
                cnt[ns] += 1

        max_req_cnt = max(cnt.values())
        ans = []
        for i, v in cnt.items():
            if v == max_req_cnt:
                ans.append(i)

        return ans
    
k, arrival, load = 3, [1,2,3], [10,12,11]
k, arrival, load = 3, [1,2,3,4], [1,2,1,2]
k, arrival, load = 3, [1,2,3,4,5], [5,2,3,3,3] 

Solution().busiestServers(k, arrival, load)