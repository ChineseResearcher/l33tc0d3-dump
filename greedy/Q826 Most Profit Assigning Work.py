# greedy - medium
from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        m, n = len(difficulty), len(worker)
        # key ideas:
        # 1) create a tuple array from difficulty and profit, and sort by both DESC
        # 2) worker also needs to be sorted to apply greedy matching

        job = [(profit[i], difficulty[i]) for i in range(m)]
        job.sort(reverse=True)
        worker.sort(reverse=True)

        # second pointer to keep track of worker assigned
        j = 0

        ans = 0
        for i in range(m):
            while j < n and worker[j] >= job[i][1]:
                ans += job[i][0]
                j += 1

            if j == n:
                break

        return ans
    
difficulty, profit, worker = [85,47,57], [24,66,99], [40,25,25]
difficulty, profit, worker = [2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]

Solution().maxProfitAssignment(difficulty, profit, worker)