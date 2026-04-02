# simulation - medium
from typing import List
class Robot:
    def __init__(self, width: int, height: int):
        self.m, self.n = height, width
        # define directions and delta
        self.p = 0
        self.positions = [0,1,2,3] # east, south, west, north
        self.pos_str = ['East','South','West','North']
        self.delta = [(0,1),(1,0),(0,-1),(-1,0)]
        # init. curr. position
        self.r, self.c = self.m-1, 0
        # count number of steps to travel one round on-edge
        self.rnd = 2 * self.m + 2 * self.n - 4
        # store corner situation
        self.corner = set([(0,0,1),(self.m-1,0,0),(self.m-1,self.n-1,3),(0,self.n-1,2)])
        # indicate if exactly k rounds are executed
        self.exact = False

    def max_move(self) -> int:
        if self.p == 0:
            return self.n-self.c-1
        elif self.p == 1:
            return self.m-self.r-1
        elif self.p == 2:
            return self.c
        elif self.p == 3:
            return self.r
            
    def step(self, num: int) -> None:
        
        # we are always travelling on the outer edge
        # so we could directly skip rounds
        num %= self.rnd

        # there's an edge case where suppose after modding num = 0
        # then we have to adjust our facing position anti-clockwise 270
        # as if we have travelled exactly (num % rnd) rounds
        if num == 0 and (self.r, self.c, self.p) in self.corner:
            self.exact = True
            return

        self.exact = False
        while num > 0:
            max_d_to_edge = self.max_move()
            if num <= max_d_to_edge:
                dr, dc = self.delta[self.p]
                self.r += dr * num
                self.c += dc * num
                return

            if self.p == 0:
                self.c = self.n-1
            elif self.p == 1:
                self.r = self.m-1
            elif self.p == 2:
                self.c = 0
            elif self.p == 3:
                self.r = 0

            self.p = (self.p - 1 + 4) % 4
            num -= max_d_to_edge 

    def getPos(self) -> List[int]:
        return [self.c, self.m-1-self.r]

    def getDir(self) -> str:
        if self.exact:
            return self.pos_str[(self.p-3+4)%4]
        return self.pos_str[self.p]
    
obj = Robot(6,3)
commands = ["step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
arguments = [[2], [2], [], [], [2], [1], [4], [], []]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))