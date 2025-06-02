# graph - hard
from typing import List
from collections import deque
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        n = len(status)
        # create another "status" array to indicate that i-th box has been found
        box_found = [0] * n
        for i in initialBoxes:
            box_found[i] = 1

        # our bfs-queue only contains boxes that are both found and unlocked
        q = deque([i for i in range(n) if status[i] == 1 and box_found[i] == 1])
        visited = set(q)

        ans = 0
        while q:

            curr_box = q.popleft()
            ans += candies[curr_box]

            seen = set()
            # mark opened
            for key in keys[curr_box]:
                status[key] = 1
                seen.add(key)
            # mark found
            for i in containedBoxes[curr_box]:
                box_found[i] = 1
                seen.add(i)

            for i in seen:
                if i not in visited and status[i] == 1 and box_found[i] == 1:
                    q.append(i)
                    visited.add(i)
            
        return ans
    
status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]

status = [1,0,0,0,0,0]
candies = [1,1,1,1,1,1]
keys = [[1,2,3,4,5],[],[],[],[],[]]
containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]
initialBoxes = [0]

Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)