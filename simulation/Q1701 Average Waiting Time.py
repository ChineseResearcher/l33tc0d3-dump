# simulation - medium
from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        n = len(customers)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) simulate the sequence of events by tracking the end time
        # of curr. active order
        # 2) waiting time for a customer = 
        # time waited before order is procesed + processing duration
        et, total = 0, 0
        for arr, duration in customers:
            total += fmax(et-arr, 0) + duration
            et = fmax(et, arr) + duration

        return total / n
    
customers = [[1,2],[2,5],[4,3]]
customers = [[5,2],[5,4],[10,3],[20,1]]
customers = [[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]

Solution().averageWaitingTime(customers)