# heap - medium
import heapq
class Solution:
    def smallestChair(self, times, targetFriend) -> int:
        # Create a list of [arrival_time, friend_index]
        minArrival = [[time[0], idx] for idx, time in enumerate(times)]
        # Heapify arrival times to process in chronological order
        # Min-heap : [arrival_time, friend_idx]
        heapq.heapify(minArrival)
        
        # Min-heap for active seating: [leaving_time, seat_no]
        activeSeating = []
        # Min-heap for available seats
        freeSeats = list(range(len(times)))  # Start with seat numbers [0, 1, 2, ...]
        heapq.heapify(freeSeats)
        
        # Leaving time dictionary for each friend
        leaving_dict = {idx: time[1] for idx, time in enumerate(times)}
        
        # Process each friend in order of arrival
        while minArrival:
            # Get next friend to arrive
            arrival_info = heapq.heappop(minArrival)
            arrival_time, friend_idx = arrival_info[0], arrival_info[1]

            # Free up seats of friends who have already left before the current arrival time
            while activeSeating and activeSeating[0][0] <= arrival_time:
                _, freed_seat = heapq.heappop(activeSeating)
                heapq.heappush(freeSeats, freed_seat)

            # Assign the smallest available seat
            assigned_seat = heapq.heappop(freeSeats)

            # Add to active seating: [leaving_time, seat_no]
            heapq.heappush(activeSeating, [leaving_dict[friend_idx], assigned_seat])

            # If this is the target friend, return their assigned seat
            # Note: there's no need for a dictionary tracking assignment
            if friend_idx == targetFriend:
                return assigned_seat
            
times, targetFriend = [[1,4],[2,3],[4,6]], 1
times, targetFriend = [[3,10],[1,5],[2,6]], 0

Solution().smallestChair(times, targetFriend)