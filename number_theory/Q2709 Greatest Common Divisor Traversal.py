# number theory - hard
from typing import List
from collections import defaultdict, deque
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
        # list down all prime factors (ignore freq) in O(sqrt(n)) time
        def unique_prime_factors(n):

            factors = set()
            # Check for factor 2
            if n % 2 == 0:
                factors.add(2)
                while n % 2 == 0:
                    n //= 2

            # Check for odd factors
            i = 3
            while i * i <= n:
                if n % i == 0:
                    factors.add(i)
                    while n % i == 0:
                        n //= i
                i += 2

            # If remaining n is a prime
            if n > 1:
                factors.add(n)

            return factors

        fac_ind = defaultdict(list)

        for idx, x in enumerate(nums): 
            for f in unique_prime_factors(x):
                fac_ind[f].append(idx)

        # build a graph amongst indices depending on
        # whether they share a common prime factor
        g = defaultdict(set)
        for f_grp in fac_ind.values():
            master = f_grp[0]
            for i in range(1, len(f_grp)):
                g[master].add(f_grp[i])
                g[f_grp[i]].add(master)

        if len(g) < len(nums):
            return False

        # use BFS to test if all indices are connected together as one
        visited = {0}

        q = deque([0])
        while q:

            node_idx = q.popleft()
            for neighbour in g[node_idx]:

                    if neighbour not in visited:
                        q.append(neighbour)
                        visited.add(neighbour)

        return len(visited) == len(nums) 
    
nums = [2,3,6]
nums = [3,9,5]
nums = [4,3,12,8]

Solution().canTraverseAllPairs(nums)