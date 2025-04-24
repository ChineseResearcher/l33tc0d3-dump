# number theory - medium
import random
class Solution:

    def __init__(self, nums):
        self.original = nums
        self.n = len(nums)

    def reset(self):
        return self.original

    def shuffle(self):

        curr = self.original[:]
        # apply the Fisher-Yates algorithm
        for i in range(0, self.n-1):
            j = random.randint(i, self.n-1)
            # swap in-place
            curr[i], curr[j] = curr[j], curr[i]
        return curr
    
obj = Solution([1,2,3])
 
commands = ["shuffle", "reset", "shuffle"]
arguments = [[], [], []]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))