# array - medium
import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.val_idx = dict()

    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False
        self.arr.append(val)
        self.val_idx[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False
        # perform an in-place swap to get the removed element to the back
        val_i, i = val, self.val_idx[val]
        val_j, j = self.arr[-1], len(self.arr)-1
        if i == j: # no swap needed
            self.arr.pop()
            del self.val_idx[val]
        else:
            self.arr[i], self.arr[j] = val_j, val_i
            self.arr.pop()
            self.val_idx[val_j] = i
            del self.val_idx[val_i]
        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr)-1)]

obj = RandomizedSet()

commands = ["remove","remove","insert","getRandom","remove","insert"]
arguments = [[0],[0],[0],[],[0],[0]]

commands = ["insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
arguments = [[1], [2], [2], [], [1], [2], []]

commands = ["insert","insert","getRandom","getRandom","insert","remove","getRandom","getRandom","insert","remove"]
arguments = [[3],[3],[],[],[1],[3],[],[],[0],[0]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))