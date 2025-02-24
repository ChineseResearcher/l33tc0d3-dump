# simulation - medium
class Solution:
    def averageWaitingTime(self, customers):
        
        # currJobEnd tracks the i-th minute at which the ongoing work ends
        # with the default to be the first arrival time
        currJobEnd = customers[0][0]
        waitingTime = []

        for customer in customers:
            arrival, process_time = customer[0], customer[1]
            waitingTime.append(max(currJobEnd - arrival, 0) + process_time)
            currJobEnd = currJobEnd + process_time if arrival <= currJobEnd else arrival + process_time

        return sum(waitingTime) / len(waitingTime)
    
customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
customers = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]

Solution().averageWaitingTime(customers)