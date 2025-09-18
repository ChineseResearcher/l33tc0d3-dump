# heap - medium
from typing import List
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        # core ideas:
        # 1) process courses while keeping track of time spent learning
        # and the courses taken, and for a new course, we could take it w/o
        # breaching the last day or we could just swap it w/ the taken course
        # that has the largest duration, and potentially reduce total time spent

        # 2) in order to optimally process the courses, sort by last day
        courses.sort(key=lambda x: x[1])

        taken, totalTime, durations = 0, 0, []
        for dur, ddl in courses:

            # take 1 more course
            if totalTime + dur <= ddl:
                taken += 1
                totalTime += dur
                heapq.heappush(durations, -dur)

            # swap course
            else:
                
                # only meaningful if we've taken a course w/
                # duration larger than the curr. course
                if durations and abs(durations[0]) > dur:
                    totalTime = totalTime - abs(durations[0]) + dur
                    heapq.heappop(durations)
                    heapq.heappush(durations, -dur)

        return taken
    
courses = [[1,2]]
courses = [[3,2],[4,3]]
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]

Solution().scheduleCourse(courses)