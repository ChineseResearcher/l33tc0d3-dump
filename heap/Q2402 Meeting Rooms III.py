# heap - hard
from typing import List
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        m = len(meetings)
        meetings.sort()

        # construct a minheap to store <available_timestamp, room_number>
        ongoing = [] 

        # second minheap storing <room_number, available_timestamp>
        # we let the n rooms be available at the start
        avail = [[i, 0] for i in range(n)]
        heapq.heapify(avail)

        # pointer to access meetings arr.
        idx = 0

        # hashtable to record reach room's assignment count (rac)
        rac = {i:0 for i in range(n)}

        # start straight from the timestamp of the earliest meeting
        t = meetings[0][0]
        while idx < m:

            # for a meeting to be qualified to be added to "avail"
            # the time (t) as of now must be at or after the earliest available room's avail. time
            while ongoing and t >= ongoing[0][0]:
                rst, room = heapq.heappop(ongoing)
                heapq.heappush(avail, [room, rst])

            # then we look at the minheap "avail" and assign curr. meeting
            # to the available room with the smallest number
            while avail and idx < m and t >= meetings[idx][0]:

                st, et = meetings[idx][0], meetings[idx][1]
                room, rst = heapq.heappop(avail)

                # since both the start time (st) of the meeting
                # and the room start time (rst) of the room are smaller than t
                # we need to correctly register the updated room usage by taking max(st, rst)
                heapq.heappush(ongoing, 
                              [max(st, rst) + (et - st), room])

                # increase counter
                rac[room] += 1
                idx += 1

            if idx == m:
                break

            # key optimisation:
            # there's no need for us to traverse each time stamp
            # we could "jump" to the next "meaningful" time stamp
            if avail:
                t = meetings[idx][0]
            else:
                t = ongoing[0][0]

        res = [[v, k] for k, v in rac.items()]
        res.sort(key = lambda x: (-x[0], x[1]))

        # the smallest room w/ the most booked count 
        return res[0][1]
    
n, meetings = 2, [[0,10],[1,5],[2,7],[3,4]]
n, meetings = 3, [[1,20],[2,10],[3,5],[4,9],[6,8]]
n, meetings = 4, [[18,19],[3,12],[17,19],[2,13],[7,10]]
n, meetings = 2, [[4,11],[1,13],[8,15],[9,18],[0,17]]
n, meetings = 2, [[43,44],[34,36],[11,47],[1,8],[30,33],[45,48],[23,41],[29,30]]

Solution().mostBooked(n, meetings)