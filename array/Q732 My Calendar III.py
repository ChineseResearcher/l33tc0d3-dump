# array - hard
class MyCalendarThree:

    def __init__(self):
        # sorted 2D arr. storing [start, end) of bookings
        self.bookings = []
        self.overlapFreq = dict()
        self.maxOverlapped = 1 # at least 1 booking -> 1 "overlapped"

    def book(self, startTime: int, endTime: int) -> int:

        newOverlap = []
        # print(self.overlapFreq)
        for s, e in self.bookings:
            # find overlapped regions
            if startTime < e and endTime > s:
                
                olvp_intvl = (max(startTime, s), min(endTime, e))
                # print(s,e,olvp_intvl)
                if olvp_intvl not in self.overlapFreq:
                    self.overlapFreq[olvp_intvl] = self.overlapFreq[(s, e)] + 1
                    newOverlap.append(list(olvp_intvl))
                else:
                    self.overlapFreq[olvp_intvl] = max(self.overlapFreq[olvp_intvl], self.overlapFreq[(s, e)] + 1)
                self.maxOverlapped = max(self.maxOverlapped, self.overlapFreq[olvp_intvl])

        # update bookings
        if (startTime, endTime) not in self.overlapFreq:
            self.bookings.append([startTime, endTime])
            self.overlapFreq[(startTime, endTime)] = 1
        
        self.bookings.extend(newOverlap)
        self.bookings.sort()

        return self.maxOverlapped

obj = MyCalendarThree()

commands = ["book", "book", "book", "book", "book", "book"]
arguments = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

commands = ["book","book","book","book","book","book","book","book","book","book"]
arguments = [[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]

commands = ["book","book","book","book","book","book","book","book","book","book"]
arguments = [[8,23],[35,48],[24,39],[10,22],[10,23],[8,22],[1,14],[36,50],[42,50],[42,50]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))