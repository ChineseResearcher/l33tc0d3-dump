# greedy - hard
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        # key ideas:
        # 1) assume we are starting with 0 energy
        # 2) we add to the amount above whenever there is a shortfall
        # relative to minimum energy required for any tasks
        # 3) we need a greedy + sorting approach to ensure the least make-up needed for shortfalls
        tasks = [(x[1]-x[0], x[1]) for x in tasks]

        # sort the tasks by
        # DESC on the diff between actual and starting, and DESC on starting
        tasks.sort(key=lambda x: (-x[0], -x[1]))

        ans, curr = 0, 0
        for diff, start in tasks:

            actual = start - diff
            if curr < start:
                ans += (start - curr)
                curr = start

            curr -= actual

        return ans

tasks = [[1,2],[2,4],[4,8]]
tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
tasks = [[1,2],[1,7],[2,3],[5,9],[2,2]]

Solution().minimumEffort(tasks)