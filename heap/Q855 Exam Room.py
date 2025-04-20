# heap - medium
import bisect
import heapq
class ExamRoom:

    def __init__(self, n: int):
        self.n = n

        # use a sorted list to keep track of occupied seats
        self.occupied = []

        # use a max heap to store <distance between nearest occupied seats, ref_seat>
        self.max_heap = []

        # due to special handling when removing first/last possible seat
        # need to maintain a set storing imaginary ref. seats
        # e.g. occupied = [0,2,4] and 0 is removed
        # we need to add an imaginary ref. seat -2 and an interval of size 4 
        # s.t. -2 + 4 // 2 = 0 when seat 0 is to be seated once again
        self.end_offset = set()

    def _find_next_occupied(self, new_seat, direction):
        # using bisect allows us to avoid linear scan when finding neighbouring occupied seats

        if direction == 'l':
            idx = bisect.bisect_left(self.occupied, new_seat)
            return self.occupied[idx-1] if idx > 0 else 0

        if direction == 'r':
            idx = bisect.bisect_left(self.occupied, new_seat)
            return self.occupied[idx] if idx < len(self.occupied) else self.n-1

    def _heap_update(self, new_seat):
        # depending on the nearest l/r occupied seat of the new seat found
        # add new possible intervals into max_heap

        l = self._find_next_occupied(new_seat, 'l')
        new_distance = new_seat - l
        new_distance = new_distance if new_distance % 2 == 0 else new_distance-1
        if new_distance > 0:
            heapq.heappush(self.max_heap, [-new_distance, l])

        r = self._find_next_occupied(new_seat, 'r')
        new_distance = r - new_seat
        new_distance = new_distance if new_distance % 2 == 0 else new_distance-1
        if new_distance > 0:
            heapq.heappush(self.max_heap, [-new_distance, new_seat])

    def seat(self) -> int:

        # if no seat taken at the point of seating query, always assign seat 0
        if not self.occupied:
            self.occupied.insert(bisect.bisect_left(self.occupied, 0), 0)
            return 0
        
        # if only one seat taken, assign the further seat as the new seat
        # then heap_update according to the new seat assigned
        if len(self.occupied) == 1:
            # 
            only_seat = self.occupied[0]
            if only_seat - 0 >= self.n - 1 - only_seat:
                new_seat = 0
            else:
                new_seat = self.n-1

            self._heap_update(new_seat)
            self.occupied.insert(bisect.bisect_left(self.occupied, new_seat), new_seat)

            return new_seat

        # internally we make use of a max heap to always get the next biggest distance
        while True:

            distance, ref_seat = heapq.heappop(self.max_heap)
            if (ref_seat in self.occupied or ref_seat in self.end_offset) \
                and ref_seat + (-distance) // 2 not in self.occupied:

                if ref_seat in self.end_offset:
                    self.end_offset.discard(ref_seat)

                break

        # invert distance to positive
        distance = -distance

        new_seat = ref_seat + distance // 2

        # update max_heap & occupied
        self._heap_update(new_seat)
        self.occupied.insert(bisect.bisect_left(self.occupied, new_seat), new_seat)

        return new_seat

    def leave(self, p: int) -> None:

        # when leave on seat p is called, it is guaranteed it is seated
        self.occupied.pop(bisect.bisect_left(self.occupied, p))

        l, r = self._find_next_occupied(p, 'l'), self._find_next_occupied(p, 'r')
        new_distance = r-l
        new_distance = new_distance if new_distance % 2 == 0 else new_distance-1

        # removing first or last seat requires special handling
        if p == 0:
            heapq.heappush(self.max_heap, [-2*r, p-r])
            self.end_offset.add(p-r)

        if p == self.n-1:
            heapq.heappush(self.max_heap, [-2*(r-l), l])
            self.end_offset.add(l)

        # left seat is used as the reference seat
        elif 0 < p < self.n-1 and new_distance > 0:
            heapq.heappush(self.max_heap, [-new_distance, l])

        return
    
obj = ExamRoom(10)
commands = ["seat","seat","seat","seat","leave","seat"]
arguments = [[],[],[],[],[4],[]]

obj = ExamRoom(10)
commands = ["seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat","seat","seat","leave"]
arguments = [[],[],[],[0],[4],[],[],[],[],[],[],[],[],[],[0]]

obj = ExamRoom(2)
commands = ["seat","seat","leave","leave","seat","seat","leave"]
arguments = [[],[],[0],[1],[],[],[1]]

obj = ExamRoom(8)
commands = ["seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat"]
arguments = [[],[],[],[0],[7],[],[],[],[],[],[],[]]

obj = ExamRoom(4)
commands = ["seat","seat","seat","seat","leave","leave","seat"]
arguments = [[],[],[],[],[1],[3],[]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command: ', command, f' With Arguments: {args}' if args else '')
    print(func(*args))