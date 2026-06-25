# dp - hard
from typing import List
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        MOD = int(1e9 + 7)
        # key ideas:
        # 1) the transitions remain unchanged. For example, for localMax -> localMin, if
        # we set the number to be 1, then it could inherit from dp[i-1][localMax][x]
        # for any 1 < x <= r, similarly for localMin -> localMax
        # 2) the transitions can be captured in r x r matrix, one for (max -> min),
        # and one for (min -> max)
        # 3) speed up the computation using fast matrix exponentiation
        # 4) the problem is symmetric, meaning if we solve Max -> Min -> ... (or Min -> Max -> ...)
        # we multiply the result by 2 to obtain the complete sum

        x = [0] * r
        for i in range(l, r+1):
            x[i-1] = 1

        T_min_max = [[0] * r for _ in range(r)]
        for i in range(r):
            for j in range(r):
                if l <= i + 1 <= r and l <= j + 1 <= r:
                    if j > i:
                        T_min_max[i][j] = 1

        T_max_min = [[0] * r for _ in range(r)]
        for i in range(r):
            for j in range(r):
                if l <= i + 1 <= r and l <= j + 1 <= r:
                    if j < i:
                        T_max_min[i][j] = 1

        ### helpers for linear algebra ###

        # multiplication of matrix
        def mat_mult(A:List[List[int]], 
                    B:List[List[int]]
                    ) -> List[List[int]]:
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
        def mat_vec_mult(A:List[List[int]],
                        x:List[int]
                        ) -> List[int]:
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
        def mat_pow(T:List[List[int]],
                    k:int
                    ) -> List[List[int]]:
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
        P = mat_mult(T_max_min, T_min_max)
        k = n - 1
        P_power_k = mat_pow(P, k // 2)
        if k % 2 == 1:
            P_power_k = mat_mult(P_power_k, T_max_min)

        final_freq = mat_vec_mult(P_power_k, x)
        return (sum(final_freq) * 2) % MOD
    
n, l, r = 3, 4, 5
n, l, r = 3, 1, 3
n, l, r = int(1e9), 1, 75 # constraint

Solution().zigZagArrays(n, l, r)