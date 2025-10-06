# heap - hard
from typing import List
import heapq
class SORTracker:

    def __init__(self):
        self.getSize = 0
        self.maxHeap, self.minHeap = [], []   

    def enc_str(self, name: str) -> List[int]:
        res = [0] * 10
        for idx, c in enumerate(name):
            res[idx] = ord(c)

        return res

    def add(self, name: str, score: int) -> None:
        if self.maxHeap:
            b_score, b_name = -self.maxHeap[0][0], self.maxHeap[0][-1]
        if self.maxHeap and (score < b_score or (score == b_score and name > b_name)):
            enc = self.enc_str(name)
            to_push = [-score] + enc + [name]
            heapq.heappush(self.maxHeap, to_push)

        # To insert into the minHeap, satisfy either:
        # 1) no elements in maxHeap
        # 2) or the addition in strictly better than max of maxheap
        else:
            enc = self.enc_str(name)
            to_push = [score] + [-o for o in enc] + [name]
            heapq.heappush(self.minHeap, to_push)
    
    def get(self) -> str:

        self.getSize += 1
        # first need to re-balance the lengths of maxheap and minheap
        # s.t. the minheap contains exactly self.getSize elements
        if len(self.minHeap) == self.getSize:
            return self.minHeap[0][-1] # the name stored

        # balancing
        while len(self.minHeap) < self.getSize:
            popped = heapq.heappop(self.maxHeap)
            # invert score + ord encodings and append the name
            to_push = [-popped[i] for i in range(1+10)] + [popped[-1]]
            heapq.heappush(self.minHeap, to_push)

        while len(self.minHeap) > self.getSize:
            popped = heapq.heappop(self.minHeap)
            to_push = [-popped[i] for i in range(1+10)] + [popped[-1]]
            heapq.heappush(self.maxHeap, to_push)

        return self.minHeap[0][-1]
    
obj = SORTracker()

commands = ["add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
arguments = [["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))