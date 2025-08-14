# heap - medium
from typing import List
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        n = len(tasks)
        # core ideas:
        # 1) first sort the tasks according to start time
        # 2) construct an auxiliary minheap to always get the next task w/
        # the shortest processing time, break tie by index
        tasks = [[info[0], info[1], idx] for idx, info in enumerate(tasks)]
        tasks.sort()
        minheap = []

        # deal w/ the first task
        # it is guaranteed to be the earliest available task
        # and the task w/ the shortest processing time needed
        currTime = tasks[0][0]

        # maintain a pointer to ref. tasks arr.
        idx = 0

        ans = []
        while True:

            if not minheap and currTime < tasks[idx][0]:
                currTime = tasks[idx][0]

            while idx < n and tasks[idx][0] <= currTime:
                _, pt, oriIdx = tasks[idx]
                heapq.heappush(minheap, [pt, oriIdx])
                idx += 1

            if idx == n:
                break
            
            pt, currAns = heapq.heappop(minheap)
            ans.append(currAns)
            # adjust time by incrementing processing time
            currTime += pt

        while minheap:
            _, currAns = heapq.heappop(minheap)
            ans.append(currAns)

        return ans
    
tasks = [[1,2],[2,4],[3,2],[4,1]]
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
tasks = [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]
tasks = [[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],
         [7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]

Solution().getOrder(tasks)