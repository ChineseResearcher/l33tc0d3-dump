# array - medium
from collections import Counter
class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.hash1 = Counter(nums1)
        self.hash2 = Counter(nums2)
        # we still need to bookkeep nums2 for add func
        self.nums2 = nums2
        
    def add(self, index: int, val: int) -> None:
        self.hash2[self.nums2[index]] -=1
        # perform add
        self.nums2[index] += val
        self.hash2[self.nums2[index]] += 1
    
    def count(self, tot: int) -> int:
        # there are at most 1000 calls to count/add
        # and max. 1000 elements in nums1, we only need to
        # scan O(1000^2) at max to find valid pairs that add up to "tot"

        cnt = 0
        for k, v in self.hash1.items():
            cnt += v * self.hash2[tot - k]
        return cnt
    
obj = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])

commands = ["count", "add", "count", "count", "add", "add", "count"]
arguments = [[7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))