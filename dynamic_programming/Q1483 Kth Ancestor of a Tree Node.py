# dp - hard
from typing import List
class TreeAncestor:
    
    def __init__(self, n: int, parent: List[int]):
        self.p = parent
        self.LOG = n.bit_length()
        self.up = [[-1] * self.LOG for _ in range(n)]
        for i, par in enumerate(self.p):
            self.up[i][0] = par

        # preprocessing + building up table
        for j in range(1, self.LOG):
            for i in range(n):
                if self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.LOG - 1, -1, -1):
            if k & (1 << i):
                if self.up[node][i] == -1:
                    return -1
                node = self.up[node][i]

        return node

obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])

commands = ["getKthAncestor", "getKthAncestor", "getKthAncestor"]
arguments = [[3,1], [5,2], [6,3]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))