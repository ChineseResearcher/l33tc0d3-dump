# binary search - medium
from typing import List
from collections import defaultdict
import bisect
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        # core ideas:
        # 1) create a sorted list of appearing index for each unique number
        # 2) use bisect to query for the frequency of a number appearing in range [l,r]
        self.num_indices = defaultdict(list)
        for idx, x in enumerate(arr):
            self.num_indices[x].append(idx)

    def query(self, left: int, right: int, value: int) -> int:

        s = bisect.bisect_left(self.num_indices[value], left)
        e = bisect.bisect_right(self.num_indices[value], right)
        return e - s
    
arr = [12,33,4,56,22,2,34,33,22,12,34,56]
obj = RangeFreqQuery(arr)

commands = ["query", "query"]
arguments = [[1,2,4], [0,11,33]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))