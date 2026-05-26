# graph - medium
from typing import List
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)

        def bfs(start_idx: int, target_val: int) -> bool:

            q, visited = deque([start_idx]), set([start_idx])
            while q:

                i = q.popleft()
                if arr[i] == target_val:
                    return True
                
                r = i + arr[i]
                if r < n and r not in visited:
                    q.append(r)
                    visited.add(r)

                l = i - arr[i]
                if l >= 0 and l not in visited:
                    q.append(l)
                    visited.add(l)

            return False

        return bfs(start, 0)

arr, start = [3,0,2,1,2], 2
arr, start = [4,2,3,0,3,1,2], 5
arr, start = [4,2,3,0,3,1,2], 0

Solution().canReach(arr, start)