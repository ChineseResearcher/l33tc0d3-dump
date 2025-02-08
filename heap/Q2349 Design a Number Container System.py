# heap - medium
import heapq
class NumberContainers:

    def __init__(self):
        # stores <idx, most recently assigned number>
        self.idxNumber = dict()
        # stores <number, min_heap of assigned indices>
        self.numberIdx = dict()
        # maintain a set storing obselete <idx, num> pairs
        self.obsolete = set()

    def change(self, index: int, number: int) -> None:
        # direct assign to index with number, override allowed
        if index in self.idxNumber:
            self.obsolete.add((index, self.idxNumber[index]))

        self.idxNumber[index] = number
        if (index, number) in self.obsolete:
            self.obsolete.discard((index, number))

        # heap push into numberIdx
        if number not in self.numberIdx:
            self.numberIdx[number] = []

        heapq.heappush(self.numberIdx[number], index)

    def find(self, number: int) -> int:
        if number not in self.numberIdx: return -1

        while self.numberIdx[number]:
            
            # curr. smallest index stored for this num
            currIdx = self.numberIdx[number][0]
            if (currIdx, number) in self.obsolete:
                heapq.heappop(self.numberIdx[number])
            else:
                return currIdx
            
        return -1
    
obj = NumberContainers()

commands = ["find", "change", "change", "change", "change", "find", "change", "find"]
arguments = [[10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))