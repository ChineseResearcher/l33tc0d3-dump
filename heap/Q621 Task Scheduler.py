# heap - medium
import heapq as hq
from collections import Counter, deque
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cooldown = deque([])
        # inverting num to build a max heap
        maxheap = [(-f, t) for t, f in Counter(tasks).items()] 
        hq.heapify(maxheap)

        task_cnt, time = 0, 0
        while maxheap or cooldown:
            
            # querying the cooldown timestamp
            if cooldown:
                if time == cooldown[0][2]: 
                    f, t, _ = cooldown.popleft()
                    hq.heappush(maxheap, (f, t))
                
            if maxheap:
                f, t = hq.heappop(maxheap)
                task_cnt += 1
                if f + 1 < 0:
                    cooldown.append((f+1, t, time+n+1))
                    
            else:
                if time < cooldown[0][2]:
                    task_cnt += 1
                
            time += 1 # time always incrementing

        return task_cnt
    
tasks, n = ["A","A","A","B","B","B"], 2
tasks, n = ["A","C","A","B","D","B"], 1
tasks, n = ["A","A","A","A","A","A","B","C","D","E","F","G"], 1

Solution().leastInterval(tasks, n)