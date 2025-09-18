# heap - medium
from typing import List
import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # construct two mappings: 1) task-user 2) task-priority
        self.tu, self.tp = dict(), dict()

        # construct maxheap <priority_i, task_i>
        self.maxheap = []

        for u, t, p in tasks:
            self.tu[t] = u
            self.tp[t] = p

            # maxheap insertion: take -ve
            heapq.heappush(self.maxheap, (-p, -t))    

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tu[taskId] = userId
        self.tp[taskId] = priority

        # push to maxheap
        heapq.heappush(self.maxheap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tp[taskId] = newPriority

        # push to maxheap
        heapq.heappush(self.maxheap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        # to remove a task, delete from both mappings
        del self.tu[taskId]
        del self.tp[taskId]

    def execTop(self) -> int:

        if not self.tu:
            return -1
        
        # to discard all tasks that may have been
        # 1) removed 2) contain outdated priority
        while self.maxheap:

            p, t = self.maxheap[0]
            t, p = abs(t), abs(p)

            if t in self.tu and self.tp[t] == p:
                break

            # otherwise, keep discarding
            heapq.heappop(self.maxheap)

        res = self.tu[t]
        # execute the valid task
        heapq.heappop(self.maxheap)

        # after execution, mark deletions
        del self.tu[t]
        del self.tp[t]
        return res
    
obj = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])

commands = ["add", "edit", "execTop", "rmv", "add", "execTop"]
arguments = [[4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))