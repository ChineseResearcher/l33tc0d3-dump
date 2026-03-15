# number theory - hard
MOD = int(1e9 + 7)
class Fancy:

    def __init__(self):
        self.arr = []
        # maintain three parameters
        self.add = 0
        self.mul = 1
        self.inv = 1

    def append(self, val: int) -> None:
        self.arr.append((val - self.add) * self.inv)

    def addAll(self, inc: int) -> None:
        self.add += inc
        self.add %= MOD

    def multAll(self, m: int) -> None:
        self.add *= m
        self.add %= MOD
        self.mul *= m
        self.mul %= MOD
        self.inv *= pow(m, -1, MOD)
        self.inv %= MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1

        return (self.arr[idx] * self.mul + self.add) % MOD

obj = Fancy()

commands = ["append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
arguments = [[2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))