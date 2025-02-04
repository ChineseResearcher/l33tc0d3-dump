# binary search - medium
class MyCalendar:

    def __init__(self):
        self.booked_start = []
        self.booked_end = []
        self.n = 0

    def bs(self, numList, num):
        # binary search helper to validate (start, end)
        n = len(numList)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2
    
            if numList[mid] == num:
                return mid
            elif numList[mid] < num:
                l = mid + 1
            elif numList[mid] > num:
                r = mid - 1
    
        return l

    def booker(self, start, end):
        self.booked_start.append(start)
        self.booked_end.append(end)
        # maintain start/end stamp order
        self.booked_start.sort()
        self.booked_end.sort()
        self.n += 1

    def book(self, start: int, end: int) -> bool:
        if not self.booked_start and not self.booked_end:
            self.booker(start, end)
            return True

        start_bs1 = self.bs(self.booked_start, start)
        start_bs2 = self.bs(self.booked_end, start)

        end_bs1 = self.bs(self.booked_start, end)
        end_bs2 = self.bs(self.booked_end, end)
        
        # instruction allows us to overlap a new start with end existing end if they are euqal
        start_equal_end = start_bs1 != start_bs2 and self.booked_end[start_bs2] == start
        start_valid = (start_bs1 == start_bs2) or start_equal_end

        # turns out (1,2) can be added to cal with (2,3), not clear in instruction
        end_valid = end_bs1 == end_bs2

        # enforce the 2nd cond. due to case where cal
        # already has (1,2) but you want to add(0,3) (not allowed)
        # start_valid & end_valid evaluated to true but start_bs1 and end_bs1 differs
        if start_valid and end_valid and start_bs1 == end_bs1:
            self.booker(start, end)
            return True
        else:
            return False
        
oobj = MyCalendar()

commands = ["book", "book", "book"]
arguments = [[10, 20], [15, 25], [20, 30]]

commands = ["book","book","book","book","book","book","book","book","book","book"]
arguments = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))