# heap - medium
import heapq
from collections import deque
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        n, m = len(servers), len(tasks)
        # key ideas:
        # 1) use one heap to store servers in-use, tracking <avail_time, idx, weight>
        # and another heap to store free servers, tracking <idx, weight>
        # 2) for each assigned task, relocate the free server to servers in-use with the new
        # available time set to max(avail_time, time of j-th task) + tasks[j]

        free, busy = [], []
        for i in range(n):
            heapq.heappush(free, (servers[i], i))

        q, ans = deque([]), []
        for j in range(m):
            q.append(tasks[j])
            # update free servers
            while busy and busy[0][0] <= j:
                _, i, w = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            while free and q:
                t = q.popleft()
                bw, bi = heapq.heappop(free)
                heapq.heappush(busy, (j + t, bi, bw))
                ans.append(bi)

        while q:
            at = busy[0][0]
            while busy and busy[0][0] == at:
                _, i, w = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            while free and q:
                t = q.popleft()
                bw, bi = heapq.heappop(free)
                heapq.heappush(busy, (at + t, bi, bw))
                ans.append(bi)

        return ans

servers, tasks = [3,3,2], [1,2,3,2,1,2]
servers, tasks = [1,2], [10,10,10,1,1,1,1]
servers, tasks = [5,1,4,3,2], [2,1,2,4,5,2,1]

Solution().assignTasks(servers, tasks)