# greedy - hard
import bisect
from typing import List
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
        n, m = len(tasks), len(workers)
        # greedy idea is to sort the tasks & workers in asc. order
        tasks.sort()
        workers.sort()

        def canComplete(k):

            # we just need k strongest workers
            w_q = workers[-k:]
            p = pills

            # target the k-easiest problems
            # Note: there's significance in iterating backwards, i.e.
            # from the most demanding k-th task instead of the forward iteration
            # this is to ensure that if a worker is able to complete tasks[i]
            # it should be the worker "just strong enough" to do it
            # ultimately, we want to avoid a situation where a great strength
            # is assigned to a trivial task which can happen in forward iteration
            for i in range(k-1, -1, -1):
                
                if w_q[-1] >= tasks[i]:
                    w_q.pop()

                # case where we need pills potentially
                else:
                    # if pill is all used up, even if some weaker workers in
                    # the pipeline can finish some less demanding tasks left, 
                    # the curr. task is already impossible to complete
                    if p == 0:
                        return False

                    # if curr. strongest worker cannot finish
                    # the curr. most demanding task, we try to see
                    # if we can find someone whose base strength >= t - strength
                    idx = bisect.bisect_left(w_q, tasks[i] - strength)

                    # if no such person exists, noted by idx == len(w_q)
                    if idx == len(w_q):
                        return False
                    
                    # use pill on the alternative person
                    p -= 1
                    w_q.pop(idx)

            return True

        # binary search on the number of tasks that can be completed
        # note: if we have m < n workers, we can only solve m problems
        l, r = 1, min(n, m)

        ans = 0
        while l <= r:

            k = (l + r) // 2
            if canComplete(k):
                ans = max(ans, k)
                l = k + 1
            else:
                r = k - 1

        return ans
    
tasks, workers, pills, strength = [3,2,1], [0,3,3], 1, 1
tasks, workers, pills, strength = [5,4], [0,0,0], 1, 5
tasks, workers, pills, strength = [10,15,30], [0,10,10,10,10], 3, 10
tasks, workers, pills, strength = [5,9,8,5,9], [1,6,4,2,6], 1, 5

Solution().maxTaskAssign(tasks, workers, pills, strength)