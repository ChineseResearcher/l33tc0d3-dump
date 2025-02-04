# array - medium
class MyCalendarTwo:

    def __init__(self):
        self.single_booked = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        # Check if the new booking would create a triple booking
        for db_start, db_end in self.double_booked:
            if start < db_end and end > db_start:  # There is an overlap with a double booking
                return False
        
        # If no triple booking, check for double bookings
        for sb_start, sb_end in self.single_booked:
            if start < sb_end and end > sb_start:  # There is an overlap with a single booking
                # Create the new interval for double booking
                overlap_start = max(start, sb_start)
                overlap_end = min(end, sb_end)
                self.double_booked.append((overlap_start, overlap_end))
        
        # Book the current interval as a single booking
        self.single_booked.append((start, end))
        
        return True
    
obj = MyCalendarTwo()

commands = ["book", "book", "book", "book"]
arguments = [[10, 20], [40, 50], [5, 45], [35, 40]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))