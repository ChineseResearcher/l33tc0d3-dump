# number theory - hard
from typing import List
from collections import defaultdict, deque
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
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

        # since all numbers are unique, we can use
        # numbers themselves as node identifiers
        for x in nums: 
            for f in unique_prime_factors(x):
                fac_ind[f].append(x)

        g = defaultdict(set)
        for f_grp in fac_ind.values():
            master = f_grp[0]
            for i in range(1, len(f_grp)):
                g[master].add(f_grp[i])
                g[f_grp[i]].add(master)

        # use BFS to compute the size of each connected component
        visited = set()

        ans = 0
        for node in nums:

            # single number w/ no other numbers that share any factor > 1
            if node not in g:
                ans = max(ans, 1)
                continue 

            if node not in visited:
                visited.add(node)
                q = deque([node])

                curr_grp_size = 0
                while q:

                    node_idx = q.popleft()
                    curr_grp_size += 1

                    for neighbour in g[node_idx]:

                            if neighbour not in visited:
                                q.append(neighbour)
                                visited.add(neighbour)

                ans = max(ans, curr_grp_size)

        return ans
    
nums = [4,6,15,35]
nums = [20,50,9,63]
nums = [2,3,6,7,4,12,21,39]

Solution().largestComponentSize(nums)