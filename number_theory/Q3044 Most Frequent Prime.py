# number theory - medium
from typing import List
from collections import defaultdict
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        # we have m x n grid where length is up to 6, implying efficient O(n^3) solution
        m, n = len(mat), len(mat[0])

        def isPrime(num):

            if num < 2:
                return False

            div = [2] + [i for i in range(3, int(num ** 0.5)+1, 2)]
            for x in div:
                if x < num and num % x == 0:
                    return False
                
            return True

        # north, north-east, ..., north-west
        delta = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

        # hashmap to store valid primes
        h = defaultdict(int)

        # go through every possible starting point
        for r in range(m):
            for c in range(n):

                # enumerate all 8 directions
                for dx, dy in delta:
                    
                    nr, nc = r, c
                    curr_num = mat[nr][nc]
                    while True:
                        
                        nr += dx
                        nc += dy

                        if not (0 <= nr < m) or not (0 <= nc < n):
                            break

                        # optimisation of obtaining the number seq.
                        curr_num = 10 * curr_num + mat[nr][nc]

                        if curr_num in h:
                            h[curr_num] += 1

                        else:
                            if curr_num > 10 and isPrime(curr_num):
                                h[curr_num] += 1

        return max(h, key=lambda k: (h[k], k)) if h else -1
    
mat = [[1,1],[9,9],[1,1]]
mat = [[9,7,8],[4,6,5],[2,8,6]]
mat = [[1,2,6],[7,9,8]]

Solution().mostFrequentPrime(mat)