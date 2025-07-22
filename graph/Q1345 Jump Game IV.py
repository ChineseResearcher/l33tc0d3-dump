# graph - hard
from typing import List
from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)
        # core idea: BFS to explore all possible paths + hashtable for same val. jump
        h = defaultdict(list)

        for i in range(n):
            h[arr[i]].append(i)

        # maintain visited
        visited = set([0]) 
        q = deque([[0,0]])

        while q:

            curr_idx, moves = q.popleft()
            if curr_idx == n-1:
                return moves

            # move to other indices of the same val.
            for j in h[arr[curr_idx]]:
                if j != curr_idx and j not in visited:
                    q.append([j, moves+1])
                    visited.add(j)
            del h[arr[curr_idx]]

            # move forward
            if curr_idx < n - 1 and (curr_idx + 1) not in visited:
                q.append([curr_idx + 1, moves+1])
                visited.add(curr_idx + 1)

            # move backward
            if curr_idx > 0 and (curr_idx - 1) not in visited:
                q.append([curr_idx - 1, moves + 1])
                visited.add(curr_idx - 1)

        return -1
    
arr = [100,-23,-23,404,100,23,23,23,3,404]
arr = [7,6,9,6,9,6,9,7]
arr = [7,7,2,1,7,7,7,3,4,1]
arr = [7] * 5 * int(1e4) + [11]

Solution().minJumps(arr)