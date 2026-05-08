# graph - medium
from typing import List
from collections import defaultdict, deque
maxN = int(1e6)
# first use Sieve to compute all prime factors for number in range [1, maxN]
pr_m = defaultdict(list)

for b in range(2, maxN + 1):
    # found another prime
    if not pr_m[b]:
        for v in range(b, maxN + 1, b):
            pr_m[v].append(b)

class Solution:
    def minJumps(self, nums: List[int]) -> int:

        n = len(nums)
        pr_grp = defaultdict(list)
        # one pass through nums to enlist all indices where nums[i] carries a prime factor
        for i, x in enumerate(nums):
            for pf in pr_m[x]:
                pr_grp[pf].append(i)

        def bfs(start: int, end: int) -> int:

            visited_idx, visited_pf = set(), set()
            visited_idx.add(start)

            q = deque([(start, 0)])
            while q:

                curr_idx, moves  = q.popleft()
                if curr_idx == end:
                    return moves
                
                x = nums[curr_idx]
                # only prime-teleport if x is a prime itself
                if x in pr_m and x not in visited_pf:
                    visited_pf.add(x)
                    for next_idx in pr_grp[x]:
                        if next_idx not in visited_idx:
                            q.append((next_idx, moves + 1))
                            visited_idx.add(next_idx)

                if curr_idx + 1 < n and (curr_idx + 1) not in visited_idx:
                    q.append((curr_idx + 1, moves + 1))
                    visited_idx.add(curr_idx + 1)

                if curr_idx - 1 >= 0 and (curr_idx - 1) not in visited_idx:
                    q.append((curr_idx - 1 , moves + 1))
                    visited_idx.add(curr_idx - 1)

        return bfs(0, n-1)
    
nums = [1,2,4,6]
nums = [4,6,5,8]
nums = [2,3,4,7,9]
nums = [1000000] * int(1e5) # constraint

Solution().minJumps(nums)