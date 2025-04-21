# prefix sum - medium
import bisect
import random
class Solution:

    def __init__(self, w):
        # build a prefix sum of weights
        rSum, self.pfSum = 0, []
        for x in w:
            rSum += x
            self.pfSum.append(rSum)
        self.sumAll = self.pfSum[-1]

    def pickIndex(self) -> int:
        sampleInt = random.randint(1, self.sumAll)
        return bisect.bisect_left(self.pfSum, sampleInt)
    
obj = Solution([1,3])

commands = ["pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
arguments = [[],[],[],[],[]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))