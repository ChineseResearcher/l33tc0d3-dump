# number theory - medium
from typing import List
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        m, n = len(groups), len(elements)
        maxSize = max(groups)

        # treat elements as the "primes" in the Sieve of Eratosthenes algorithm
        composites = dict()

        for i in range(n):

            if elements[i] in composites:
                continue

            curr = elements[i]
            while curr <= maxSize:

                # mark the smallest index i s.t. it is divisible elements[i]
                if curr not in composites:       
                    composites[curr] = i

                curr += elements[i]

        ans = []
        for i in range(m):

            if groups[i] in composites:
                ans.append(composites[groups[i]])
            else:
                ans.append(-1)

        return ans
    
groups, elements = [8,4,3,2,4], [4,2]
groups, elements = [2,3,5,7], [5,3,3]
groups, elements = [10,21,30,41], [2,1]

Solution().assignElements(groups, elements)