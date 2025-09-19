# array - medium
from typing import Tuple
class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [ [0] * 26 for _ in range(rows) ]

    def parse(self, f:str) -> Tuple[str, str]:
        res = f[1:].split('+')
        return res[0], res[1]

    def getVal(self, exp:str) -> int:

        # if first char is in range [0,25] when taking
        # relative order to ord('A'), then this is a cell reference
        # otherwise, it's an integer
        if 0 <= ord(exp[0]) - ord('A') <= 25:
            val = self.grid[int(exp[1:])-1][ord(exp[0]) - ord('A')]
        else:
            val = int(exp)

        return val

    def setCell(self, cell: str, value: int) -> None:
        self.grid[int(cell[1:])-1][ord(cell[0]) - ord('A')] = value

    def resetCell(self, cell: str) -> None:
        self.grid[int(cell[1:])-1][ord(cell[0]) - ord('A')] = 0

    def getValue(self, formula: str) -> int:
        p1, p2 = self.parse(formula)
        return self.getVal(p1) + self.getVal(p2)
    
obj = Spreadsheet(3)

commands = ["getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
arguments = [["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))