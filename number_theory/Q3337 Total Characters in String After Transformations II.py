# number theory - hard
from typing import List
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # since we only have 26 alphabets, the transition matrix size is of fixed 26 by 26
        T = [ [0] * 26 for _ in range(26) ]

        # build the transition matrix T
        for i in range(26):

            # nums[i] denotes the count of consecutive alphabets that
            # letters[i] is going to transition into
            for j in range(i+1, i+nums[i]+1):
                T[j % 26][i] += 1

        # init. our starting vector w/ frequencies of char in s
        x = [0] * 26
        for char in s:
            x[ord(char) - ord('a')] += 1

        ### helpers for linear algebra ###
        MOD = int(1e9 + 7)
        # multiplication of matrix
        def mat_mult(A, B):
            # A, B are N×N
            N = len(A)

            C = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    s = 0
                    for k in range(N):
                        s += (A[i][k] * B[k][j]) % MOD
                    C[i][j] = s

            return C

        # multiplication of vector and matrix
        def mat_vec_mult(A, x):
            # A is N × N, x is 1 x N
            N = len(A)

            y = [0] * N
            for i in range(N):
                s = 0
                for j in range(N):
                    s += (A[i][j] * x[j]) % MOD
                y[i] = s

            return y

        # fast exponentiation of matrix
        def mat_pow(T, k):
            # Compute T^k in O(N^3 log k)
            # Start with identity matrix
            N = len(T)
            result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]

            base = T
            while k > 0:
                if k & 1:
                    result = mat_mult(result, base)
                base = mat_mult(base, base)
                k >>= 1

            return result

        ### computing results using helpers ###
        T_power_k = mat_pow(T, t)
        final_freq = mat_vec_mult(T_power_k, x)

        return sum(final_freq) % MOD
    
s, t, nums = "abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
s, t, nums = "azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# testing efficiency
s, t, nums = "abcyy", int(1e9), [1,1,1,1,25,1,25,1,25,1,1,25,1,25,1,25,1,25,1,1,1,1,1,1,1,2]

Solution().lengthAfterTransformations(s, t, nums)