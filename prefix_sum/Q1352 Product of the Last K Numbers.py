# prefix sum - medium
import bisect
class ProductOfNumbers:

    def __init__(self):
        # maintain an ordered indices at which we encountered num 0
        self.zero_pos = []

        # prefix sum variables
        self.prefix_sum = []
        self.curr_sum = 1
        
    def add(self, num: int) -> None:
        
        # build prefix sum
        # 1) if num is 0, repeat the last curr_sum
        # 2) if num in non-0, build curr_sum with num
        if num != 0:
            self.curr_sum *= num
        
        self.prefix_sum.append(self.curr_sum)

        # add idx to zero_pos if num is 0
        if num == 0: 
            self.zero_pos.append(len(self.prefix_sum)-1)

    def getProduct(self, k: int) -> int:
        # we want to check if the index for the last k-th element
        # does include any 0s at OR to its right by ref. zero_pos
        k_idx = len(self.prefix_sum) - k

        res = bisect.bisect_left(self.zero_pos, k_idx)
        if res <= len(self.zero_pos)-1:
            return 0
        
        # if there are only n prefix sums, and we want the last n product
        if k_idx-1 < 0: return self.prefix_sum[-1]
        
        return int(self.prefix_sum[-1] / self.prefix_sum[k_idx-1])     

obj = ProductOfNumbers()

commands = ["add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
arguments = [[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

commands = ["add","getProduct","getProduct","add","add","getProduct","add","getProduct","add","getProduct","add","getProduct","getProduct","add","getProduct"]
arguments = [[7],[1],[1],[4],[5],[3],[4],[4],[3],[4],[8],[1],[6],[2],[3]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))