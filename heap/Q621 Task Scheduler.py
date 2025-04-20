# heap - medium
import heapq as hq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n) -> int:

        cooldown_queue = deque([])
        # inverting num to build a max heap
        task_freq = [(-f, t) for t, f in Counter(tasks).items()] 
        hq.heapify(task_freq)

        task_cnt, time = 0, 0
        # debug_queue = []

        while task_freq or cooldown_queue:
            
            # querying the cooldown timestamp
            if cooldown_queue and time == cooldown_queue[0][2]: 
                f, t, _ = cooldown_queue.popleft()
                hq.heappush(task_freq, (f, t))
                
            if task_freq:
                f, t = hq.heappop(task_freq)
                # debug_queue.append(t)
                task_cnt += 1
                if f + 1 < 0:
                    cooldown_queue.append((f+1, t, time+n+1))
                    
            elif not task_freq and time < cooldown_queue[0][2]:
                # debug_queue.append('_')
                task_cnt += 1
                
            time += 1 # time always incrementing

        return task_cnt
    
tasks, n = ["A","A","A","B","B","B"], 2
tasks, n = ["A","C","A","B","D","B"], 1
tasks, n = ["A","A","A","A","A","A","B","C","D","E","F","G"], 1

Solution().leastInterval(tasks, n)