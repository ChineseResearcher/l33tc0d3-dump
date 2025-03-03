# heap - hard
import heapq
class MedianFinder:
    # this problem is a tricky application of two heaps (min & max) working
    # together so that we can always get the median in O(logN) time

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # when both heaps are empty, add to max_heap first
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return
        
        # otherwise, insert the number by comparing
        # between max/min value
        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # we make sure that the size of max_heap
        # is always the size of min_heap or plus one
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        return

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]
        
obj = MedianFinder()

commands = ["addNum", "addNum", "findMedian", "addNum", "findMedian"]
arguments = [[1], [2], [], [3], []]

commands = ["addNum", "addNum", "addNum", "addNum", "findMedian"]
arguments = [[2], [5], [7], [3], []]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))