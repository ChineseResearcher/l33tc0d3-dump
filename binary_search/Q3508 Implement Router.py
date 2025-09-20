# binary search - medium
from typing import List
from collections import deque, defaultdict
import bisect
class Router:

    def __init__(self, memoryLimit: int):
        # addPacket might breach memory limit, 
        # monitoring of master queue length is needed
        self.ml = memoryLimit

        # define master queue
        self.master_q = deque([])

        # define queue by destination(s)
        self.dest_q = defaultdict(deque)

        # define a set to validate active packet
        self.active = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        src, dest, ts = source, destination, timestamp

        # duplicate
        if (src, dest, ts) in self.active:
            return False
        
        # add to both master & dest queues
        self.master_q.append((src, dest, ts))
        self.dest_q[dest].append((src, ts))

        # mark active
        self.active.add((src, dest, ts))

        # monitor memory limit, get rid of oldest packet if needed
        if len(self.master_q) > self.ml:
            p_src, p_dest, p_ts = self.master_q.popleft()
            # remove from active
            self.active.remove((p_src, p_dest, p_ts))
            self.dest_q[p_dest].popleft()

        return True

    def forwardPacket(self) -> List[int]:

        # if empty q
        if not self.master_q:
            return []
    
        # FIFO retrieval
        p_src, p_dest, p_ts = self.master_q.popleft()
        # remove from active
        self.active.remove((p_src, p_dest, p_ts))

        # when a packet is forwarded from the master queue
        # it's also guaranteed that it's at the front of deque by destination
        self.dest_q[p_dest].popleft()

        return [p_src, p_dest, p_ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:

        dest, st, et = destination, startTime, endTime

        # use bisect for quick lookup
        r = bisect.bisect_right(self.dest_q[dest], et, key=lambda t: t[1])
        l = bisect.bisect_left(self.dest_q[dest], st, key=lambda t: t[1])

        return r-l
    
obj = Router(3)

commands = ["addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
arguments = [[1,4,90], [2,5,90], [1,4,90], [3,5,95], [4,5,105], [], [5,2,110], [5,100,110]]

obj = Router(2)

commands = ["addPacket", "forwardPacket", "forwardPacket"]
arguments = [[7,4,90], [], []]

obj = Router(2)

commands = ["addPacket","forwardPacket","addPacket","addPacket","getCount","getCount","getCount"]
arguments = [[5,1,1],[],[3,5,1],[5,1,1],[5,1,1],[1,1,1],[1,1,1]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))