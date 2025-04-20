# heap - medium
import heapq
class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        # idea is to always fetch the next class with a most increment in pass ratio
        # if an extra sure pass student is to be assigned to it
        max_heap = [[-((x[0]+1) / (x[1] + 1) - x[0] / x[1])] + x for x in classes]
        heapq.heapify(max_heap)

        while extraStudents > 0:
            
            _, curr_pass, curr_total = heapq.heappop(max_heap)  
            # calculate the next increment percentage after adding one extra student
            next_increment = -((curr_pass+2)/(curr_total+2) - (curr_pass+1)/(curr_total+1))
            heapq.heappush(max_heap, [next_increment, curr_pass+1, curr_total+1])
            
            # mark assignment of student
            extraStudents -= 1
            
        return sum([x[1]/x[2] for x in max_heap]) / len(max_heap)
    
classes, extraStudents = [[1,2],[3,5],[2,2]], 2
classes, extraStudents = [[2,4],[3,9],[4,5],[2,10]], 4

Solution().maxAverageRatio(classes, extraStudents)